import sys
import os
import aiohttp
import asyncio
import json
import time
import piexif
import piexif.helper

from src.logging import success, warning, error, StatusPrinter
from src.snap import Snap

try:
    from win32_setctime import setctime # try importing windows-only library
except:
    pass

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

# removes duplicates based on mid parameter
def deduplicate(snaps):
    seen = []
    for snap in snaps:
        if snap.mid not in seen:
            seen.append(snap.mid)
            yield snap

def filter_not_downloaded(snaps):
    list_of_files = []
    list_of_mids = []

    for file in os.scandir('memories'):
        list_of_files.append(file.name)
        if file.name.split(".")[-1] == 'jpg':
            mid = piexif.helper.UserComment.load(piexif.load(file.path)['Exif'][piexif.ExifIFD.UserComment])
            list_of_mids.append(mid)
    
    # filter out snaps by m_ids and (for videos) by filenames
    snaps = [snap for snap in snaps if snap.get_mid_exif() not in list_of_mids and (snap.base_name + snap.extension) not in list_of_files]
    return snaps

# makes post request to get the download link
async def make_initial_request(session, snap):
    req = await session.post(snap.url)
    response = await req.text()
    return response

# retrieve the download link
async def make_download_request(session, url):
    req = ''
    try:
        req = await session.get(url)
        file = await req.read()
        return file
    except:
        raise Exception(f'Could not download: {req}')

async def download_single_snap(session, snap, printer):
    response = await make_initial_request(session, snap)

    if response == '':
        print('\n\n')
        error('Could not download', snap.base_name)
        warning('If this error persists request new data\n')
        return

    file = await make_download_request(session, response)
    already_downloaded = False

    # verify if already existing file is indeed the same
    if os.path.exists(snap.get_filename()):
        counter = 1
        filename_copy = snap.base_name

        # create temporary file for video duplicates
        temp_name = 'memories/' + str(time.time())
        if snap.extension == '.mp4':
            with open(temp_name, 'wb') as f:
                f.write(file)

        # incrementally change filename for bulk-downloaded stories
        while os.path.exists(snap.get_filename()):
            # skip if saved media_id is the same as incoming one
            if snap.extension == '.jpg' and snap.mid == snap.get_mid_exif():
                already_downloaded = True
                break

            # skip if local file has the same size as incoming one
            if snap.extension == '.mp4':
                new_size = os.path.getsize(temp_name)
                local_size = os.path.getsize(snap.get_filename())

                if new_size == local_size:
                    already_downloaded = True
                    break
            
            # increment filename suffix
            snap.base_name = filename_copy + f'_{counter:02}'
            counter += 1
        
        # remove temporary file
        if snap.extension == '.mp4':
            os.remove(temp_name)

    # download if file is not a duplicate
    if not already_downloaded:
        with open(snap.get_filename(), 'wb') as f:
            f.write(file)
            
        timestamp = snap.timestamp.timestamp()
        os.utime(snap.get_filename(), (timestamp, timestamp))
        if os.name=='nt':   # only for windows overrite creation time
            setctime(snap.get_filename(), timestamp)
        
        # add date information to EXIF information of image for support in cloud services (Amazon Photos, Google Photos, etc.)
        if snap.extension == '.jpg':
            snap.save_exif()

        printer.update()
    
async def download_memories(path, sort):
    clear()

    # load json content
    with open(path, 'r') as f:
        content = json.load(f)
        media = content['Saved Media']

    # start from the oldest ones 
    if sort:
        media.reverse()

    if not os.path.exists('memories'):
        try:
            os.mkdir('memories')
            success('Directory created\n')
        except Exception as e:
            error('Could not create directory', e)
            exit()

    snaps = []
    for item in media:
        snaps.append(Snap(item))      
    
    snaps = list(deduplicate(snaps))    # remove duplicates
    success(f'Found {len(snaps)} files')

    already_downloaded = len(os.listdir('memories'))
    printer = StatusPrinter(already_downloaded, len(snaps))

    snaps = filter_not_downloaded(snaps)   # remove already downloaded
    
    # asynchronous file downloading
    timeout = aiohttp.ClientTimeout(total=6000)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        await asyncio.gather(*[
            download_single_snap(session, snap, printer) for snap in snaps
        ])

    print('\n\n----------------\n')
    success('Finished')
    input('\nSaved you a lot of time? Buy me a coffee: https://www.buymeacoffee.com/maciekk')
    sys.exit()
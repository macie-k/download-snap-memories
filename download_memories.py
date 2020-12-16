import json
import requests
import os
import datetime
import urllib

from sys import exit
from argparse import ArgumentParser
from colorama import Fore
from colorama import Style
from tqdm import tqdm
from find_duplicates import save_duplicates

try:
    from win32_setctime import setctime
except: # for linux
    pass

def downloadMemories(path):
    clear()

    with open(path, 'r') as f:
        content = json.load(f)
        media = content['Saved Media']

    success(f'Found {len(media)} files')

    if not os.path.exists('memories'):
        try:
            os.mkdir('memories')
            success('Directory created\n')
        except Exception as e:
            error('Could not create directory', e)
            exit()

    media.reverse() # start from the oldest ones

    for data in tqdm(media, desc=f"{Fore.GREEN}[OK]{Style.RESET_ALL} Downloading: ", unit="file", ncols=70, bar_format="{desc}{n_fmt}/{total_fmt} {bar} {percentage:3.0f}%"):
        date = data['Date']
        url = data['Download Link']
        filetype = data['Media Type']

        day = date.split(" ")[0]
        time = date.split(" ")[1].replace(':', '-')
        filename = f'memories/{day}_{time}'
        extension = '.mp4' if filetype == 'VIDEO' else '.jpg'

        req = requests.post(url, allow_redirects=True)
        response = req.text

        if response == '':
            print('\n\n')
            error('Could not download', filename[9:])
            warning('If this error persists request new data\n')
            continue

        downloaded = False
        if os.path.exists(filename+extension):
            dw_size = urllib.request.urlopen(response).info()['Content-Length']
            
            counter = 1
            filename_copy = filename

            while os.path.exists(filename+extension):
                local_size = str(os.path.getsize(filename+extension))
                if local_size == dw_size:
                    downloaded = True
                    break
                
                if counter == 1:
                    filename += '_01'
                    counter += 1
                    continue

                filename = filename_copy + f'_{counter:02}'
                counter += 1

        if not downloaded:
            file = requests.get(response)
            
            filename += extension
            with open(filename, 'wb') as f:
                f.write(file.content)
                
            timestamp = datetime.datetime.timestamp(datetime.datetime.strptime(day + '-' + time, "%Y-%m-%d-%H-%M-%S"))
            os.utime(filename, (timestamp, timestamp))
            if os.name=='nt':   ## only for windows overrite creation time
                setctime(filename, timestamp)

    print('\n\n----------------\n')
    success('Finished')
    return media

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def success(str, as_input=False):
    output = f'{Fore.GREEN}[OK]{Style.RESET_ALL} {str}'
    if as_input:
        input(output)
    else:
        print(output)

def warning(str, as_input=False):
    output = f'{Fore.YELLOW}[!]{Style.RESET_ALL} {str}'
    if as_input:
        input(output)
    else:
        print(output)

def error(str, e='', as_input=False):
    output = f'{Fore.RED}[ERROR]{Style.RESET_ALL} {str}: {e}'
    if as_input:
        input(output)
    else:
        print(output)

parser = ArgumentParser()
parser.add_argument('-d', '--find-duplicates', dest='duplicates', action='store_true', default=None, help='Direct login info')

args = parser.parse_args()

try:
    path = 'memories_history.json' if not os.path.exists('json') else 'json/memories_history.json'
    media = downloadMemories(path)

    if args.duplicates:
        save_duplicates(media)
        success('Saved duplicates')

    input()
    exit()
except Exception as e:
    error('Execption occured', e, True)

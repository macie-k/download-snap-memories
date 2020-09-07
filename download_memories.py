import json
import requests
import os
import datetime

from win32_setctime import setctime

def downloadMemories(path):
    clear()

    with open(path, 'r') as f:
        content = json.load(f)
        media = content['Saved Media']
        print(f'[OK] Found {len(media)} files')

        if not os.path.exists('memories'):
            try:
                os.mkdir('memories')
                print('[OK] Directory created\n')
            except Exception as e:
                input(f'[ERROR] Could not create directory: {e}')
                exit()

        index = 1
        for data in media:

            date = data['Date']
            url = data['Download Link']
            filetype = data['Media Type']

            day = date.split(" ")[0]
            time = date.split(" ")[1].replace(':', '-')
            filename = f'memories/{day}_{time}.mp4' if filetype == 'VIDEO' else f'memories/{day}_{time}.jpg'

            if not os.path.exists(filename):
                print(f'[OK] Downloading [{index}/{len(media)}]\r', end="")

                req = requests.post(url, allow_redirects=True)
                response = req.text
                file = requests.get(response)
                timestamp = datetime.datetime.timestamp(datetime.datetime.strptime(day + '-' + time, "%Y-%m-%d-%H-%M-%S"))

                with open(filename, 'wb') as f:
                    f.write(file.content)
                os.utime(filename, (timestamp, timestamp))
                if os.name=='nt':   ## only for windows overrite creation time
                    setctime(filename, timestamp)
            index += 1
        print('\n\n---------------- ')
        input('[OK] Finished ')
        exit()

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

try:
    path = 'json/memories_history.json' if os.path.exists('json') else 'memories_history.json'
    downloadMemories(path)
except Exception as e:
    print('[ERROR] ', e)
    input()

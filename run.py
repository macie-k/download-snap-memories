from src.download_memories import download_memories
from src.logging import error
from sys import exit
from argparse import ArgumentParser

import asyncio
import os

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-s', '--sort', action='store_true', help='Download memories in chronological order')
    args = parser.parse_args()

    try:        
        path = 'memories_history.json' if not os.path.exists('json') else 'json/memories_history.json'
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download_memories(path, args.sort))

        input()
        exit()
    except Exception as e:
        print()
        error('Exception occured', e, True)

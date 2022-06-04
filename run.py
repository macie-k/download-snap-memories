from src.download_memories import download_memories
from src.logging import error
from sys import exit
from argparse import ArgumentParser

import asyncio
import src.download_memories as dm

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-s', '--sort', action='store_true', help='Download memories in chronological order')
    parser.add_argument('-d', '--dir', nargs=1, type=str, help='Select target directory')
    parser.add_argument('--show-errors', action='store_true', help='Show full error stack')
    args = parser.parse_args()

    if args.dir: 
        dm.target_dir = args.dir[0]
        if dm.target_dir[-1] != '/':
            dm.target_dir += '/'

    if not args.show_errors:
        try:                
            loop = asyncio.get_event_loop()
            loop.run_until_complete(download_memories(args.sort))

            input()
            exit()
        except Exception as e:
            print()
            error('Exception occured', e, True)

    #####################################################

    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_memories(args.sort))

    input()
    exit()
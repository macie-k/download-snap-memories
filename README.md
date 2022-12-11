# Download snapchat memories
Download all memories from Snapchat  

<br>  
<br>  

<p align="center">
  <a href="http://bit.ly/BuyMeACoffee-GitHub" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60px">
  </a>  
</p>

<br>  

## Download
- Download the latest release [here](https://bit.ly/snap-mem-releases)

<br>

## Update
Snapchat now allows you to download memories directly from their page by selecting `Do you want to include your memories as a downloadable file?` option. It will split your memories into multiple `.zip` files and will not name them properly, but it will allow you to download overlays (text, drawings) from that snaps. So choose what fits you.  

For the script to work properly, don't select this option, but also uncheck `Filter your export by date range` field, to download all memories.

<br>

## Preview

<p align="">
  <img width="auto" height="auto" src="https://user-images.githubusercontent.com/25122875/102345128-2a7a3700-3f9d-11eb-8d5a-6e4970913a89.png">
</p>

<br>

## How to
- [Video](https://bit.ly/33OqDQI) tutorial <br><br>
- Go [here](https://accounts.snapchat.com/accounts/downloadmydata) and request your data
- Wait for the e-mail from Snapchat & download the archive
- Place `memories_history.json` file in the same directory as `run.py` or `download_memories.exe` files
- Launch the program

<br>

## Launching
- Windows:
  - Just download the `.exe` file
  - Alternatively install python 3.x, run `pip install -r requirements.txt` to install dependencies and then `python run.py` <br><br>
- [Linux instructions](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_linux_instructions.md)
- [macOS instructions](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_mac_instructions.md)
- [Android instructions](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_android_instructions.md)

<br>

## Arguments
- `-s` `--sort`   Download snaps in chronological order
- `-d` `--dir`    Specify target directory
- `--show-errors` Show full error stack

<br>

## Sidenotes
- Since version `1.15.0`, files are being downloaded much faster, meaning you can get rate limited, in that case just retry after few minutes
- macOS users will likely get an SSL error, [here](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_mac_instructions.md) is the solution
- `Invalid URL ‘ ‘ : No schema supplied` means the links in your json have expired, just request the data again
- Windows will likely block the executable as it's unsigned

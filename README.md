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
- Download the latest release [here](http://ceesty.com/eamtOE)

<br>

## Preview

<p align="">
  <img width="auto" height="auto" src="https://user-images.githubusercontent.com/25122875/102345128-2a7a3700-3f9d-11eb-8d5a-6e4970913a89.png">
</p>

<br>

## How to
- [Video](http://ceesty.com/eamaJb) tutorial <br><br>
- Go [here](https://accounts.snapchat.com/accounts/downloadmydata) and request your data
- Wait for the e-mail from Snapchat & download the archive
- Place `memories_history.json` file in the same directory
- Launch the program

<br>

## Launching
- Windows:
  - Just download the `.exe` file
  - Alternatively install python 3.x and run `pip install -r requirements.txt` to install dependencies <br><br>
- [Linux](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_linux_instructions.md)
- [macOS](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_mac_instructions.md)
- [Android](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_android_instructions.md)

<br>

## Duplicates
- Warning about duplicates means that the `.json` file contains multiple entries for the exact same file
- Usually that means everything was downloaded correctly, but for your information skipped duplicates were saved to a file
- You can verify the memories by manually downloading them via the `.html` file and comparing to those from the `memories` folder

<br>

## Sidenotes
- macOS users will very likely get an SSL error, [here](https://github.com/emermacko/download-snap-memories/blob/master/docs/run_mac_instructions.md) is the solution
- `Invalid URL ‘ ‘ : No schema supplied` means the links in your json have expired, just request the data again
- Windows will likely block the executable as it's unsigned
- Don't place both `json` folder and `memories_history.json` in the same directory

# Running instructions for Android phones

<br>

- Download and launch [Termux](https://play.google.com/store/apps/details?id=com.termux)
- Run the following commands
```bash
$ termux-setup-storage
$ cd storage/downloads
$ mkdir github && cd github
$ pkg install git
$ git clone https://github.com/emermacko/download-snap-memories.git
$ cd download-snap-memories
$ pip3 install -r requirements.txt
```
- Now go to your file manager and copy the `memories_history.json` file into the `downloads/github/download-snap-memories` folder
  - Or do it via the command line if you're feeling adventurous
- And now back to Termux, run the command:
```
$ python3 download_memories.py
```

<br>

## Sidenotes
- You will need to grant the `Storage` permission to Termux app
- Some folder names may (but shouldn't) be different, so you may have to correct the commands yourself
- 4th command `mkdir github && cd github` is optional, just to keep the things organized
- No idea what is the minimum android required, can confirm it works on `10`

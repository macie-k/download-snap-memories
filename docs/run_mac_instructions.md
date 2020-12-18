# Installing and running for macOS

<br>

## Below information is based on this [issue](https://github.com/emermacko/download-snap-memories/issues/4)

<br>

## Python

- First download homebrew for mac:
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

- Download python3 from homebrew for mac
```shell
brew install pyenv
pyenv install --list
pyenv install 3.9.0
```

## Libraries
- Navigate to script's folder
- Install using `pip3 install -r requirements.txt`

## Running
- Navigate to script's folder
- To run the script just use `python3 download_memories.py`

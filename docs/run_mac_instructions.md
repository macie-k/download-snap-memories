# Installing and running for macOS

<br>

## Below information is based on [this](https://github.com/emermacko/download-snap-memories/issues/4) issue

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
- To run the script just use `python3 run.py`

## SSL Error
If you encounter SSL certificate error try running either of these commands:
```bash
$ pip3 install certifi
$ /Applications/Python\ 3.x/Install\ Certificates.command
```
or
``` bash
$ sudo /Applications/Python\ 3.x/Install\ Certificates.command
```
In both cases replace the `x` with your version, you can check it using
```bash
$ python --version
```

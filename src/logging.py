from colorama import Fore, Style
from tqdm import tqdm

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

# status bar printing
class StatusPrinter:
    def __init__(self, initial, amount):
        self.index = 0      # current index
        self.bar = tqdm(    # bar object with properties
            total=amount,
            desc=f"{Fore.GREEN}[OK]{Style.RESET_ALL} Downloading: ",
            ncols=70,
            bar_format="{desc}{n_fmt}/{total_fmt} {bar} {percentage:3.0f}%")
        self.bar.update(initial)    # update bar value to match already downloaded

    def update(self):
        self.bar.update(1)
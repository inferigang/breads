from rich import print
from random import choice
from requests import get
from requests.exceptions import RequestException

from urllib3 import disable_warnings
disable_warnings()

def get_random_color() -> str:
    ''' Returns a random color from a predefined list '''
    
    color_list: list = [
        "cyan", "yellow", "red"
    ]
    
    return choice(color_list)

def get_version() -> None:
    ''' Prints the current version of BREADS '''
    
    current_version = """
Breaking Active Directory Security
v1.0-dev ~ by: inferigang"""

    print(f"[bold {get_random_color()}]{current_version}[/]\n")

def get_banner() -> None:
    ''' Return BREADS banner url '''

    banner_list: list = [
        "https://pastebin.com/raw/tgZ4qpKD",
        "https://pastebin.com/raw/8RZ1Lgwf",
        "https://pastebin.com/raw/CUJJ1KJu",
        "https://pastebin.com/raw/dYLkjP83",
        "https://pastebin.com/raw/GWgXMfty",
        "https://pastebin.com/raw/wvPRwqSZ"
    ]

    banner = choice(banner_list)

    try:
        response = get(banner, verify=False)
        banner = response.text

        print(f"[bold {get_random_color()}]{banner}[/]")
        return get_version()
    except RequestException as error:
        print(f"[red]✖ Could not retrive banner from pastebin: {error}[/]")
        pass

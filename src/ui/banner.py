from rich import print
from random import choice
from requests import get
from requests.exceptions import RequestException

from urllib3 import disable_warnings
disable_warnings()

def get_random_color() -> str:
    ''' Returns a random color from a predefined list '''
    
    color_list: list = [
        "cyan", "yellow", "red", "blue", "white", "magenta", "green",
        "italic cyan", "italic yellow", "italic red", "italic blue", "italic white", "italic magenta", "italic green",
        "bold cyan", "bold yellow", "bold red", "bold blue", "bold white", "bold magenta", "bold green",
    ]
    
    return choice(color_list)

def get_banner() -> None:
    ''' Return BREADS banner url '''

    banner_list: list = [
        "https://pastebin.com/raw/mhEASUuU",
        "https://pastebin.com/raw/CFEzbcVh",
        "https://pastebin.com/raw/yVe8AAud",
        "https://pastebin.com/raw/iKR7qDAM",
        "https://pastebin.com/raw/fSzQMQ27",
        "https://pastebin.com/raw/kGqfqWRc"
    ]

    banner = choice(banner_list)

    try:
        response = get(banner, verify=False)
        banner = response.text

        current_version = "Breaking Active Directory Security by @opps3c\nVersion: v1.1.4"
        print(f"[bold {get_random_color()}]{banner}\n{current_version}\n\nType 'help' to list commands[/]")

    except RequestException as error:
        print(f"[red][!][/][bright_white] Error when requesting banner from pastebin: {error}[/]")
        pass

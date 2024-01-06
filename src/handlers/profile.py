from rich import print
from rich.prompt import Prompt

from os import mkdir, path, listdir, environ
from uuid import uuid4

import json

from src.helpers.user import BREADS_FOLDER, get_current_profile

PROFILE_UUID = uuid4().hex

def create_breads_directory() -> None:
    ''' Create .breads directory on user home, if not exists '''

    if not path.exists(BREADS_FOLDER):
        mkdir(BREADS_FOLDER)
        print("[green][+][/] [bright_white].breads folder created in user home directory[/]")
        return True
    else:
        print("[yellow][!][/] [bright_white].breads folder already exists on user home directory[/]")
        pass

def create_profile_folder() -> None:
    ''' Create the profile folder name based on user input in /home/user/.breads/profile_name/ '''

    global profile_name

    profile_name_input = Prompt.ask("[yellow]# Type the profile name[/]")
    profile_name = profile_name_input

    print(f"\n[green][✔][/] [bright_white]Creating [b]{profile_name}'s[/] profile folder [/]")
    create_breads_directory()

    folder_name = f"{BREADS_FOLDER}/{profile_name}"

    if not path.exists(folder_name):
        mkdir(folder_name)
        print(f"[green][+][/] [bright_white]{folder_name} folder created[/]")
        create_profile_base_json()
    else:
        print(f"[red][!][/] [bright_white]{folder_name} profile already exists[/]")
        return

def create_profile_base_json() -> None:
    ''' Create the base JSON file to be used by the profile to store the information collected '''

    base_profile = {
        "profile_name": profile_name,
        "profile_uuid": PROFILE_UUID,
        "host": "",
        "username": "",
        "password": ""
    }

    base_profile_json_path: str = f"{BREADS_FOLDER}/{profile_name}/settings.json"

    try:
        with open(base_profile_json_path, 'w') as base_profile_json:
            json.dump(base_profile, base_profile_json, ensure_ascii=False, indent=4)
            base_profile_json.truncate()

            print(f"[green][+][/] [bright_white]Created base profile JSON file ({base_profile_json_path})[/]")
            print(f"[yellow][!][/] [bright_white]Profile name: [b]{profile_name}[/] - UUID: [b]{PROFILE_UUID}[/][/]")

    except Exception as error:
        print(f"[red][!][/] [bright_white]Error when trying to create the base profile JSON file: {error}[/]")
        return False


def load_profile() -> None:
    ''' Loads a profile based on user input if at least one exists on breads '''

    if not path.exists(BREADS_FOLDER):
        print(f"[red][!][/] .breads directory not found\n")
        return

    if path.exists(BREADS_FOLDER):

        folders_list = listdir(BREADS_FOLDER)

        if not folders_list:
            print(f"[red][!][/] No profiles found on .breads directory. Create one with 'create_profile' command\n")
            return

        for folder_name in folders_list:
            print(f"[cyan]* {folder_name}[/]")

        load_user_input = Prompt.ask("\n# Type the profile name to be used")
        for folder_name in folders_list:

            if(load_user_input == folder_name):
                print(f"[green][+][/] [bright_white]Profile [b]{folder_name}'s[/b] selected successfully![/]")
                environ["breads_profile"] = folder_name

                profile_json_file = f"{BREADS_FOLDER}/{get_current_profile()}/settings.json"

                with open(profile_json_file, 'r+') as json_file:
                    existing_data = json.load(json_file)

                    host     = existing_data['host']
                    username = existing_data['username']
                    password = existing_data['password']

                    if(len(host) > 2): # If the length of host variable on profile json file is greater than 2 we can assume we already have an host defined
                        print(f"[yellow][!][/] [bright_white]Profile settings: {host}, {username}, {password}[/]")
                        keep_data_input = Prompt.ask("[yellow][!][/] [bright_white]There is already information stored in this profile, do you want to keep it? [Y/N][/]")
                        keep_data_input = keep_data_input.lower()

                        if(keep_data_input == 'y'):
                            print("[yellow][!][/] [bright_white]Not changing current configuration[/]\n")
                            return
                        else:
                            pass

                    target_host_input = Prompt.ask("# Type the target host (ex: 127.0.0.1)")
                    username_input    = Prompt.ask("# Type the username to be used (example.lab/Administrator)")
                    password_input    = Prompt.ask("# Type the password to be used")

                    profile_data = {
                        "host": target_host_input,
                        "username": username_input,
                        "password": password_input
                    }

                    try:
                        existing_data.update(profile_data)
                        json_file.seek(0)
                        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
                        json_file.truncate()

                        print(f"[green][+][/] [bright_white]Profile information stored successfully![/]\n")
                    except Exception as error:
                        print(f"[red][!][/] [bright_white]Error when trying to store profile information: {error}[/]")
            else:
                print(f"[red][!][/] [bright_white]Profile not found, check if the name is correct[/]")

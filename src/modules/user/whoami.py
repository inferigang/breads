from rich import print

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_user_whoami(inp) -> None:
    ''' Return information from a specific user from the domain (sAMAccountName, distinguishedName, Groups, and UAC value)'''
    username: str = inp

    if len(username) == 0:
        print("[red][✖] You need to specify a username to use 'whoami' command [/]")
        return

    search_filter = f'(&(objectClass=user)(sAMAccountName={username}))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!] Getting {username} account information[/]")

        for dn, attributes in query:
            for attr_name in attributes:

                attributes_list = {
                    'sAMAccountName': 'Username', 
                    'distinguishedName': 'Account DN',
                    'memberOf': 'Account Groups',
                    'userAccountControl': 'UAC Value'
                }

                for attribute, name in attributes_list.items():
                        if(attr_name == attribute):
                            for attribute_name in attributes[attr_name]:

                                print(f"[cyan]* {name}: {attribute_name.decode('utf-8')} [/]")

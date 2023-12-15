from rich import print

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_pass_not_req() -> None:
    ''' Get users from domain that does not require a password to authenticate '''


    search_filter = f'(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!] Getting password not required users[/]\n")

        for dn, attrs in query:
            for attr_name in attrs:
                if attr_name == 'sAMAccountName' and dn is not None:
                    for user_name in attrs[attr_name]:
                        print(f"[green]{user_name.decode('utf-8')}")

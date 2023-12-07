from rich import print

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_pass_not_req() -> None:

    search_filter = f'(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))'
    query = connect_and_fetch(search_filter)

    if query:
        for dn, attrs in query:
            if not dn == None:
                print(f"[green][✔] Username: {dn}")
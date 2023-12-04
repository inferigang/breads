from rich import print

import json
import ldap

from handlers.ldap_connect import connect_and_fetch

def get_all_users() -> None:
    search_filter = f'(&(objectCategory=person)(objectClass=user))'
    
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!] Getting all users from domain... [/]")
        for dn, attrs in query:
            for attr_name in attrs:
                if attr_name == 'sAMAccountName' and dn is not None:
                    for user_name in attrs[attr_name]:
                        print(f"[green]{user_name.decode('utf-8')}")

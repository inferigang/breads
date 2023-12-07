from rich import print

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_admins() -> None:

        search_filter = f'(&(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))(adminCount=1))'
        query = connect_and_fetch(search_filter)

        if query:
            print(f"[yellow][!] Getting administrator(s) username(s)... [/]")
            print(f"[bold red][:] WARNING: Users listed below are not necessarily Domain Administrators [/]")

            for dn, attrs in query:
                for attr_name in attrs:
                    if(attr_name == 'sAMAccountName') and not dn == None:
                        for admin_name in attrs[attr_name]:
                            print(f"[green][✔] Administrator username: {admin_name.decode('utf-8')}")

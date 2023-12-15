from rich import print

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_domain_controllers() -> None:
    ''' Get all the Domain Controllers name '''

    search_filter = '(primaryGroupID=516)' # 516 is the Primary ID for Domain Controllers computers
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!] Getting domain controllers name... [/]\n")

        for dn, attrs in query: # dn is just here to be possible to get the attrs from the query
            for attr_name in attrs:
                if(attr_name == 'name'):
                    for dc_name in attrs[attr_name]:
                        print(f"[green][✔] Domain Controller name: {dc_name.decode('utf-8')}")

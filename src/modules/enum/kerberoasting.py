from rich import print 

import json
import ldap

from src.handlers.ldap_connect import connect_and_fetch

def get_kerberoastable() -> None:
    ''' Search for kerberoastable users with filter and ignore krbtgt or computers'''

    # TO-DO: Return kerberoastable user hash

    # https://github.com/byt3bl33d3r/CrackMapExec/blob/3c3e412193cb6d3237abe90c543e5d995bfa4447/cme/protocols/ldap.py#L927C1-L927C1
    search_filter = "(&(servicePrincipalName=*)(UserAccountControl:1.2.840.113556.1.4.803:=512)" "(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(!(objectCategory=computer)))"

    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!] Getting kerberoastable users from domain (excluding computers)[/]")
        print("[bold red][:] WARNING: If the result is blank, there is no kerberoastable users to be listed [/]\n")


        for dn, attrs in query:
            for attr_name in attrs:

                attributes_list = {
                        'sAMAccountName': 'Username',
                        'servicePrincipalName': 'SPN'
                }

                for attr, name in attributes_list.items():
                    if (attr_name == attr):
                        for attr_name in attrs[attr_name]:
                            print(f"[cyan]* {name}: {attr_name.decode('utf-8')} [/]")

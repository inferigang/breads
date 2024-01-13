from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

MODULE_PROTOCOL = ['ldap']

def get_kerberoastable() -> None:
    ''' Search for kerberoastable users with filter and ignore krbtgt or computers'''

    # TO-DO: Return kerberoastable user hash
    # https://github.com/byt3bl33d3r/CrackMapExec/blob/3c3e412193cb6d3237abe90c543e5d995bfa4447/cme/protocols/ldap.py#L927C1-L927C1
    
    search_filter = "(&(servicePrincipalName=*)(!(objectCategory=computer)))"
    attributes = ['sAMAccountName', 'servicePrincipalName']
    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] [bright_white]Kerberoastable users from domain (excluding computers):[/]")
        print("[yellow][!][/] [bright_white]If the result is blank, there is no kerberoastable users to be listed [/]")


        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:

                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

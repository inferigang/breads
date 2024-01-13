from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_disabled_users() -> None:
    ''' List all the current disabled accounts from the domain '''

    search_filter = f'(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))'
    attributes = ['sAMAccountName']
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] Disabled Domain Users:")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

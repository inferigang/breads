from rich import print
from src.handlers.ldap_connect import connect_and_fetch

MODULE_PROTOCOL = ['ldap']

def get_admins() -> None:
    ''' Get all the accounts from domain that has administrator privilege in somewhere '''

    search_filter = f'(&(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))(adminCount=1))'
    attributes = ['sAMAccountName']
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Administrator(s) username(s):[/]")
        print(f"[yellow][!][/] Users listed below are not necessarily Domain Administrators, they can be Local Administrator.")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

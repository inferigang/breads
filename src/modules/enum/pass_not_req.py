from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_pass_not_req() -> None:
    ''' Get users from domain that does not require a password to authenticate '''

    search_filter = f'(&(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=32))'
    attributes = 'sAMAccountName'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] Users that doesn't require any password to logon:")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

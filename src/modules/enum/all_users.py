from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_users() -> None:
    ''' List all usernames from the domain'''

    search_filter = f'(&(objectCategory=person)(objectClass=user))'
    attributes = ['sAMAccountName']
    query = connect_and_fetch(search_filter)

    if query: 
        print(f"[yellow][!][/] Domain Users:")
        
        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[bright_white]{value}[/]")

from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_all_disabled_users() -> None:
    ''' List all the current disabled accounts from the domain '''

    search_filter = f'(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=2))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] Disabled Domain Users:")

        for dn, attrs in query:
            for attr_name in attrs:
                if(attr_name == 'sAMAccountName') and not dn == None:
                    for user_name in attrs[attr_name]:
                        print(f"[bright_white]{user_name.decode('utf-8')}[/]")

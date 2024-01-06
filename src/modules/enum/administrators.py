from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_admins() -> None:
    ''' Get all the accounts from domain that has administrator privilege in somewhere '''

    search_filter = f'(&(&(objectCategory=person)(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))(adminCount=1))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Administrator(s) username(s):[/]")
        print(f"[yellow][!][/] Users listed below are not necessarily Domain Administrators, they can be Local Administrator.")

        for dn, attrs in query:
            for attr_name in attrs:
                if(attr_name == 'sAMAccountName') and not dn == None:
                    for admin_name in attrs[attr_name]:
                        print(f"[bright_white]{admin_name.decode('utf-8')}[/]")

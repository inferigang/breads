from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_domain_controllers(inp) -> None:
    ''' Get all the Domain Controllers name '''

    #search_filter = '(primaryGroupID=516)' # 516 is the Primary ID for Domain Controllers computers
    search_filter = '(&(objectCategory=Computer)(userAccountControl:1.2.840.113556.1.4.803:=8192))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Domain Controller(s) Name(s):[/]")

        for _dn, attrs in query:
            for attr_name in attrs:

                if(attr_name == 'dNSHostName'):
                    for dc_name in attrs[attr_name]:

                        print(f"[bright_white]{dc_name.decode('utf-8')}[/]")

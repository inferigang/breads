from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_domain_controllers() -> None:
    ''' Get all the Domain Controllers name '''

    search_filter = '(primaryGroupID=516)' # 516 is the Primary ID for Domain Controllers computers
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Domain Controller(s) Name(s):[/]")

        for dn, attrs in query: # dn is just here to be possible to get the attrs from the query
            for attr_name in attrs:
                if(attr_name == 'name'):
                    for dc_name in attrs[attr_name]:
                        print(f"[green][+][/] [bright_white]Name: {dc_name.decode('utf-8')}[/]")

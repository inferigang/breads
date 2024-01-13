from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

MODULE_PROTOCOL = ['ldap']

def get_computers() -> None:
    ''' Return all the computers that can be located on the environment'''
    
    search_filter = "(&(objectClass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))"
    attributes = ['sAMAccountName', 'name', 'operatingSystem', 'dNSHostName']
    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] [bright_white]All computers located:[/]")
        print("[yellow][!][/] [bright_white]If the result is blank, there is no computer(s) to be listed [/]")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

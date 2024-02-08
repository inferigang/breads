from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

MODULE_PROTOCOL = ['ldap']

def get_trusted_delegate() -> None:
    ''' Retrieve all the accounts that has msds-allowedtodelegateto enabled '''
    
    search_filter = "(userAccountControl:1.2.840.113556.1.4.803:=524288)"
    
    attributes = ['sAMAccountName']
    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] [bright_white]All accounts with msDS-AllowedToDelegateTo located:[/]")
        print("[yellow][!][/] [bright_white]If the result is blank, there is no accounts or computers with msDS-AllowedToDelegateTo rights [/]")


        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

# Credits: https://github.com/Pennyw0rth/NetExec/pull/41/files

from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

MODULE_PROTOCOL = ['ldap']

def get_obsolete() -> None:
    ''' Search for for obsolete operating systems installed on computers'''
    
    search_filter = ("(&(objectclass=computer)(!(userAccountControl:1.2.840.113556.1.4.803:=2))"
                         "(|(operatingSystem=*Windows 6*)(operatingSystem=*Windows 2000*)"
                         "(operatingSystem=*Windows XP*)(operatingSystem=*Windows Vista*)"
                         "(operatingSystem=*Windows 7*)(operatingSystem=*Windows 8*)"
                         "(operatingSystem=*Windows 8.1*)(operatingSystem=*Windows Server 2003*)"
                         "(operatingSystem=*Windows Server 2008*)(operatingSystem=*Windows Server 2000*)))")
    
    attributes = ['name', 'operatingSystem', 'dNSHostName']
    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] [bright_white]Obsolete operating systems installed on computers located:[/]")
        print("[yellow][!][/] [bright_white]If the result is blank, there is no obsolete operating systems installed on computers to be listed [/]")


        for dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

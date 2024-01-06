from rich import print
from rich.console import Console
console = Console()

from src.handlers.ldap_connect import connect_and_fetch

def get_pass_policy() -> None:
    ''' Get the current password policy from the domain '''
    
    search_filter = f'(objectClass=domainDNS)'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Domain Password Policy:[/]")

        for dn, attributes in query:
            for attr_name in attributes:

                attributes_list = {
                    'minPwdLength': 'Minimum Password Length', 
                    'lockoutThreshold': 'Lockout Threshold', 
                    'lockoutDuration': 'Lockout Duration (Milliseconds)',
                }

                for attribute, name in attributes_list.items():
                        if(attr_name == attribute):
                            for attribute_name in attributes[attr_name]:
                                console.print(f"[green][+][/] [bright_white]{name}: {attribute_name.decode('utf-8')}[/]", highlight=False)

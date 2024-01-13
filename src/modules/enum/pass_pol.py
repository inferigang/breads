from rich import print
from rich.console import Console
console = Console()

from src.handlers.ldap_connect import connect_and_fetch

def get_pass_policy() -> None:
    ''' Get the current password policy from the domain '''
    
    search_filter = f'(objectClass=domainDNS)'
    attributes = ['minPwdLength', 'lockoutThreshold', 'lockoutDuration']
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] [bright_white]Domain Password Policy:[/]")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:
                        
                        for value in values[attribute]:
                            value = value.decode('utf-8')

                            if attribute == 'lockoutThreshold' and value == '0':
                                console.print(f"[green][+][/] [bright_white]{attribute}:[/] [bright_yellow]{value} - Password Spray possiblity detected[/]", highlight=False)
                            else:
                                console.print(f"[green][+][/] [bright_white]{attribute}: {value}[/]", highlight=False)


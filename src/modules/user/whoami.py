# Time is stored in Windows Filetime and starts in January 1, 1601 as we can see on https://learn.microsoft.com/en-us/windows/win32/api/minwinbase/ns-minwinbase-filetime?redirectedfrom=MSDN

from rich import print
from rich.console import Console
console = Console()

from src.handlers.ldap_connect import connect_and_fetch
from src.helpers.filetime_to_date import filetime_to_dt

def get_user_whoami(inp) -> None:
    ''' Return information from a specific user from the domain (sAMAccountName, distinguishedName, Groups, UAC value and status, Last Logon and Last Logoff time)'''
    username: str = inp

    if len(username) == 0:
        print("[red][!][/] You need to specify a username to use 'whoami' command")
        return

    search_filter = f'(&(objectClass=user)(sAMAccountName={username}))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] Whoami: {username}")

        for dn, attributes in query:
            for attr_name in attributes:

                attributes_list = {
                    'sAMAccountName': 'sAMAccountName', 
                    'distinguishedName': 'distinguishedName',
                    'memberOf': 'Member of',
                    'lastLogon': 'Last Logon (Nanoseconds)',
                    'lastLogoff': 'Last Logoff' ,
                    'userAccountControl': 'UAC Value'
                }

                uac_values = {
                    '512': 'User is Enabled - Password Expires',
                    '514': 'User is Disabled - Password Expires',
                    '66048': "User is Enabled - [bold yellow]Password Never Expires[/]",
                    '66050': "User is Disabled - [bold yellow]Password Never Expires[/]"
                }

                for attribute, name in attributes_list.items():
                        if(attr_name == attribute):
                            for attribute_value in attributes[attr_name]:
                                if "userAccountControl" in attr_name:
                                    for uac_number, uac_context in uac_values.items():
                                        if attribute_value.decode('utf-8') == uac_number:
                                            console.print(f"[green][+][/] UAC Status: [bright_white]{uac_context}[/]", highlight=False)

                                if "lastLogon" in attr_name:
                                        last_logon_filetime = attribute_value.decode('utf-8')
                                        last_login_datetime = filetime_to_dt(int(last_logon_filetime))

                                        console.print(f"[green][+][/] Last Logon: [bright_white]{last_login_datetime}[/]", highlight=False)

                                if "lastLogoff" in attr_name:
                                        last_logoff_filetime = attribute_value.decode('utf-8')

                                        if last_logoff_filetime == 0:
                                            console.print(f"[green][+][/] Last Logoff: [bright_white]{last_logoff_filetime}[/]", highlight=False)
                                        else:
                                            last_logoff_datetime = filetime_to_dt(int(last_logoff_filetime))
                                            console.print(f"[green][+][/] Last Logoff: [bright_white]{last_logoff_datetime}[/]", highlight=False)

                                else:
                                    print(f"[green][+][/] {name}: [bright_white]{attribute_value.decode('utf-8')}[/]")

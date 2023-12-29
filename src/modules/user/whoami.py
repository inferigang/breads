from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_user_whoami(inp) -> None:
    ''' Return information from a specific user from the domain (sAMAccountName, distinguishedName, Groups, and UAC value)'''
    username: str = inp

    if len(username) == 0:
        print("[red][✖] You need to specify a username to use 'whoami' command [/]")
        return

    search_filter = f'(&(objectClass=user)(sAMAccountName={username}))'
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!] Getting {username} account information[/]\n")

        for dn, attributes in query:
            for attr_name in attributes:

                attributes_list = {
                    'sAMAccountName': 'Username', 
                    'distinguishedName': 'Account DN',
                    'memberOf': 'Account Groups',
                    'userAccountControl': 'UAC Value'
                }

                uac_values = {
                    '512': 'Enabled - Password Expires',
                    '514': 'Disabled - Password Expires',
                    '66048': "Enabled - Password Doesn't Expires",
                    '66050': "Disabled - Password Doesn't Expires"
                }

                for attribute, name in attributes_list.items():
                        if(attr_name == attribute):
                            for attribute_value in attributes[attr_name]:

                                if "userAccountControl" in attr_name:
                                    for uac_number, uac_context in uac_values.items():
                                        if attribute_value.decode('utf-8') == uac_number:
                                            print(f"[green][✔] User Account Control (UAC): {uac_context}[/]")
                                else:
                                    print(f"[green][✔] {name}: {attribute_value.decode('utf-8')}[/]")

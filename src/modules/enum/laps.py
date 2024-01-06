from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_laps(inp) -> None:
    ''' Get all the LAPS password from domain pass'''

    computer_name: str = inp

    global search_filter

    if len(computer_name) == 0:
        search_filter = "(&(objectCategory=computer)(|(msLAPS-EncryptedPassword=*)(ms-MCS-AdmPwd=*)(msLAPS-Password=*)))"
    else:
        search_filter = "(&(objectCategory=computer)(|(msLAPS-EncryptedPassword=*)(ms-MCS-AdmPwd=*)(msLAPS-Password=*))(name=" + computer_name + "))"

    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] LAPS information:")
        print(f"[yellow][!][/] If the result is blank, probably there is no LAPS information to retrive or your user does not have the required permissions\n")

        for dn, attributes in query:
            for attr_name in attributes:

                attributes_list = {
                    'msLAPS-EncryptedPassword': 'Computer Encrypted Password', 
                    'msLAPS-Password': 'Computer Password',
                    'ms-MCS-AdmPwd': 'Administrator Password',
                    'sAMAccountName': 'Computer Name'
                }

                for attribute, name in attributes_list.items():
                        if(attr_name == attribute):
                            for attribute_name in attributes[attr_name]:

                                print(f"[green][+][/] [bright_white]{name}: {attribute_name.decode('utf-8')} [/]")

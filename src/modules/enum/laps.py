from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_laps(inp) -> None:
    ''' Get all the LAPS password from domain pass'''

    computer_name: str = inp

    global search_filter

    if len(computer_name) == 0:
        search_filter = "(&(objectCategory=computer)(|(msLAPS-EncryptedPassword=*)(ms-MCS-AdmPwd=*)(msLAPS-Password=*)))"
    else:
        search_filter = f"(&(objectCategory=computer)(|(msLAPS-EncryptedPassword=*)(ms-MCS-AdmPwd=*)(msLAPS-Password=*))(name={computer_name}))"

    attributes = ['sAMAccountName', 'msLAPS-Password', 'ms-MCS-AdmPwd', 'msLAPS-EncryptedPassword']
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] LAPS information:")
        print(f"[yellow][!][/] If the result is blank, probably there is no LAPS information to retrive or your user does not have the required permissions\n")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:

                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

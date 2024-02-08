from rich import print
from src.handlers.ldap_connect import connect_and_fetch

def get_adcs() -> None:
    ''' Retrieve the PKI Enrollment Servers from domain '''

    global search_filter

    search_filter = '(objectClass=pKIEnrollmentService)'

    attributes = ['dNSHostName', 'cn', 'msPKI-Enrollment-Servers']
    query = connect_and_fetch(search_filter)

    if query:
        print(f"[yellow][!][/] Querying the PKI Enrollment Servers:")
        print(f"[yellow][!][/] If the result is blank, probably there is no PKI Enrollment Servers to retrive or your user does not have the required permissions\n")

        for _dn, values in query:
            for attribute_name in values:

                for attribute in attributes:
                    if attribute_name == attribute:

                        for value in values[attribute]:
                            value = value.decode('utf-8')
                            print(f"[green][+][/] [bright_white]{attribute}: {value}[/]")

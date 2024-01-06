from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

def get_kerberoastable() -> None:
    ''' Search for kerberoastable users with filter and ignore krbtgt or computers'''

    # TO-DO: Return kerberoastable user hash
    # https://github.com/byt3bl33d3r/CrackMapExec/blob/3c3e412193cb6d3237abe90c543e5d995bfa4447/cme/protocols/ldap.py#L927C1-L927C1
    
    search_filter = "(&(servicePrincipalName=*)(UserAccountControl:1.2.840.113556.1.4.803:=512)" "(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(!(objectCategory=computer)))"
    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] [bright_white]Kerberoastable users from domain (excluding computers):[/]")
        print("[yellow][!][/] [bright_white]If the result is blank, there is no kerberoastable users to be listed [/]")


        for dn, attrs in query:
            for attr_name in attrs:

                attributes_list = {
                        'sAMAccountName': 'Username',
                        'servicePrincipalName': 'SPN'
                }

                for attr, name in attributes_list.items():
                    if (attr_name == attr):
                        for attr_name in attrs[attr_name]:
                            print(f"[bright_white]{name}: {attr_name.decode('utf-8')}[/]")

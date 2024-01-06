from rich import print 
from src.handlers.ldap_connect import connect_and_fetch

def get_maq_acc_quota() -> None:
    ''' Get the Macchine Account Quota value domain-level attribute '''

    search_filter = "(objectClass=*)"
    query_attribute = "ms-DS-MachineAccountQuota"

    query = connect_and_fetch(search_filter)

    if query:
        print("[yellow][!][/] Domain Machine Account Quota value:")
       
        for dn, attrs in query:
            for attr_name in attrs:
                if(attr_name == query_attribute):
                    for maq_account_quota_value in attrs[attr_name]:
                        print(f"[green][+][/] [bright_white]Machine Account Quota value: {maq_account_quota_value.decode('utf-8')} [/]")

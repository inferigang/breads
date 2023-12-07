from rich import print

import json
import ldap

from src.handlers.profile import BREADS_FOLDER
from src.helpers.user import get_current_profile
from src.handlers.ldap_connect import connect_and_fetch

def get_pass_policy() -> None:

        search_filter = f'(objectClass=domainDNS)'
        query = connect_and_fetch(search_filter)

        if query:
            print(f"[yellow][!] Getting domain password policy[/]")

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
                                    print(f"[cyan]* {name}: {attribute_name.decode('utf-8')} [/]")

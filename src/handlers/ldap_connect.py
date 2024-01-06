from rich import print

import json
import ldap

from src.handlers.profile import BREADS_FOLDER
from src.helpers.user import get_current_profile

def connect_and_fetch(search_filter):
    if get_current_profile() == 'None':
        print("[red][!][/] You need to load a profile first, use 'load_profile' command")
        return False
    
    settings_json_file = f"{BREADS_FOLDER}/{get_current_profile()}/settings.json"
    
    with open(settings_json_file, 'r') as settings_file:
        data = json.load(settings_file)

        hostname = data['host']
        username = data['username']
        password = data['password']

        baseDN = username.split('/')[0]
        ldap_username = f"{username.split('/')[1]}@{baseDN}"

        baseDN = "DC=" + ",DC=".join(baseDN.split("."))
        ldapURI = f"ldaps://{hostname}"

        username = username.split('/')[1]  # Get the actual username without the domain

        print(f"[yellow][!][/] [bright_white]Connecting to {ldapURI} as [b]{username}:{password}[/]\n")

        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        ldap.set_option(ldap.OPT_REFERRALS, 0)
        
        connect = ldap.initialize(ldapURI)
        connect.set_option(ldap.OPT_REFERRALS, 0)    
        connect.simple_bind_s(ldap_username, password)

        search_scope = ldap.SCOPE_SUBTREE

        try:
            query = connect.search_s(baseDN, search_scope, search_filter)
            return query
        
        except ldap.LDAPError as error:
            print(f"[red][!][/] [bright_white]LDAP Error: {error}[/]")
        
        finally:
            connect.unbind_s()
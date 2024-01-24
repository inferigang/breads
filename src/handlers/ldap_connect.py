from rich import print
from rich.progress import Progress

import json
import ldap
from ldap.controls import SimplePagedResultsControl

from src.handlers.profile import BREADS_FOLDER
from src.helpers.user import get_current_profile

def connect_and_fetch(search_filter, page_size=100):
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

        username = username.split('/')[1]  # Get the actual username without the FQDN

        print(f"[yellow][!][/] [bright_white]Connecting to {ldapURI} as [b]{username}:{password}[/]")

        with Progress() as progress:
            task = progress.add_task("[cyan][*][/] [bright_white]Executing command[/]\n", total=100)

            while not progress.finished:
                progress.update(task, advance=10)

                ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
                
                connect = ldap.initialize(ldapURI)
                connect.set_option(ldap.OPT_REFERRALS, 0)
                connect.simple_bind_s(ldap_username, password)

                search_scope = ldap.SCOPE_SUBTREE

                try:
                    total_results = []
                    req_ctrl = SimplePagedResultsControl(criticality=True, size=page_size, cookie='')

                    while True:
                        query = connect.search_ext(baseDN, search_scope, search_filter, serverctrls=[req_ctrl])
                        
                        rtype, rdata, rmsgid, serverctrls = connect.result3(query)
                        total_results.extend(rdata)

                        pctrls = [c for c in serverctrls if c.controlType == SimplePagedResultsControl.controlType]
                        if pctrls:
                            if pctrls[0].cookie:
                                req_ctrl.cookie = pctrls[0].cookie
                            else:
                                break
                        else:
                            break

                    progress.update(task, advance=40)
                    return total_results
                
                except ldap.LDAPError as error:
                    print(f"[red][!][/] [bright_white]LDAP Error: {error}[/]")
                
                finally:
                    connect.unbind_s()
                    progress.update(task, advance=50)
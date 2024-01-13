#!/usr/bin/python3

from cmd import Cmd
from rich import print
from datetime import datetime

import os

from src.ui.banner import get_banner
from src.handlers.profile import create_profile_folder, load_profile
from src.helpers.user import get_current_profile

from src.modules.enum.domain_controllers import get_domain_controllers
from src.modules.enum.administrators import get_admins
from src.modules.enum.pass_not_req import get_pass_not_req
from src.modules.enum.pass_pol import get_pass_policy
from src.modules.enum.all_users import get_users
from src.modules.enum.disabled_accounts import get_disabled_users
from src.modules.enum.laps import get_laps
from src.modules.enum.kerberoasting import get_kerberoastable
from src.modules.enum.maq_acc_quota import get_maq_acc_quota
from src.modules.enum.obsolete import get_obsolete
from src.modules.enum.all_computers import get_computers
from src.modules.enum.trusted_delegation import get_trusted_delegate

from src.modules.user.whoami import get_user_whoami

class BreadsPrompt(Cmd):

    current_time = datetime.now().time()
    current_time = current_time.strftime('%H:%M:%S')

    prompt = f"{current_time} - breads # "
    intro = get_banner()

    def emptyline(self):
        pass
        
    def do_exit(self, inp):
        ''' Exit the program '''
        print(f"[red][✖] Exiting... [/]")
        return True

    def do_banner(self, inp):
        ''' Return a random banner from get_banner function '''
        get_banner()

    def do_create_profile(self, inp):
        ''' Create a new profile to be used by BREADS '''
        create_profile_folder()

    def do_load_profile(self, inp):
        ''' Load an profile based on user input, if exists '''
        load_profile()

    def do_get_current_profile(self, inp):
        ''' Return the current profile loaded by the user '''
        print(get_current_profile())

    def do_get_dcs(self, inp):
        ''' Return domain controllers machine name '''
        get_domain_controllers()

    def do_get_admins(self, inp):
        ''' Return administrators usernames '''
        get_admins()

    def do_get_pass_not_req(self, inp):
        ''' Return all users that does need a password to login '''
        get_pass_not_req()

    def do_get_pass_pol(self, inp):
        ''' Get the current domain password policy (Minimum Password Length, Lockout Threshold and Lockout Duration)'''
        get_pass_policy()

    def do_get_users(self, inp):
        ''' Get all the accounts username from the domain '''
        get_users()

    def do_get_disabled_users(self, inp):
        ''' Get all the disabled accounts from the domain '''
        get_disabled_users()

    def do_whoami(self, inp):
        ''' Get information from specific user account '''
        get_user_whoami(inp)

    def do_laps(self, inp):
        ''' Get LAPS information from all computers or one specific '''
        get_laps(inp)

    def do_kerberoasting(self, inp):
        ''' Search for kerberoastable users with filter and ignore krbtgt'''
        get_kerberoastable()

    def do_get_maq_account_quota(self, inp):
        ''' Retrive the Machine Account Quota value from the domain '''
        get_maq_acc_quota()

    def do_get_obsolete(self, inp):
        ''' Search for for obsolete operating systems installed on computers '''
        get_obsolete()

    def do_get_computers(self, inp):
        ''' Retrive all the computers that can be located on the domain '''
        get_computers()

    def do_trusted_delegate(self, inp):
        ''' Retrieve all the accounts that has msds-allowedtodelegateto enabled '''
        get_trusted_delegate()

    # Allow user to exit from the prompt using CTRL+D
    do_EOF = do_exit

BreadsPrompt().cmdloop()
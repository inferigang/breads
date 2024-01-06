#!/usr/bin/python3

from cmd import Cmd
from rich import print

from src.ui.banner import get_banner
from src.handlers.profile import create_profile_folder, load_profile
from src.helpers.user import get_current_profile

from src.modules.enum.domain_controllers import get_domain_controllers
from src.modules.enum.administrators import get_admins
from src.modules.enum.pass_not_req import get_pass_not_req
from src.modules.enum.pass_pol import get_pass_policy
from src.modules.enum.all_users import get_all_users
from src.modules.enum.disabled_accounts import get_all_disabled_users
from src.modules.enum.laps import get_laps
from src.modules.enum.kerberoasting import get_kerberoastable
from src.modules.enum.maq_acc_quota import get_maq_acc_quota

from src.modules.user.whoami import get_user_whoami

class BreadsPrompt(Cmd):

    prompt = f"breads # "
    intro = get_banner()

    def emptyline(self):
        pass

    def complete_modules(self, text, line, begidx, endidx):
        
        _AVAILABLE_MODULES = [
            'banner', 
            'create_profile', 
            'load_profile', 
            'get_current_profile', 
            'get_dcs', 
            'get_das', 
            'get_pass_not_req',
            'get_pass_pol',
            'get_all_users',
            'get_all_disabled_users'
            'whoami'
            'laps'
            'kerberoasting'
        ]

        return [i for i in _AVAILABLE_MODULES if i.startswith(text)]
        
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

    def do_get_all_users(self, inp):
        ''' Get all the accounts username from the domain '''
        get_all_users()

    def do_get_all_disabled_users(self, inp):
        ''' Get all the disabled accounts from the domain '''
        get_all_disabled_users()

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

    # Allow user to exit from the prompt using CTRL+D
    do_EOF = do_exit

BreadsPrompt().cmdloop()

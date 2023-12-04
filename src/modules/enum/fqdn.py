# Not done yet, based on Impacket modules
# We can use a LDAP query that will get the domainDns attributes and retrieve the "dn" value...

# def get_domain_fqdn() -> None:

#     if(get_current_profile()) == 'None':
#         print("[red][✖] You need to load a profile first, use 'load_profile' command [/]")
#         return False

#     with open(f'{BREADS_FOLDER}/{get_current_profile()}/settings.json', 'r') as settings_file:
#         data = json.load(settings_file)

#         hostname = data['host']
#         username = data['username']
#         password = data['password']

#         domain = username.split('/')[0] # Get the actual domain without the slash
#         username = username.split('/')[1] # Get the actual username without the slash

#         print(f"\n[cyan]* Host: {hostname}\n* User: {username}\n* Pass: {password}\n* Domain: {domain}\n[/]")

#         conn = smbconnection.SMBConnection(remoteName=hostname, remoteHost=hostname, myName=None, sess_port=445)
#         conn.login(username, password, domain=domain)

#         rpc_con = transport.DCERPCTransportFactory(rf'ncacn_np:{hostname}[\pipe\samr]')
#         rpc_con.set_credentials(username, password)

#         try:
#             rpc_con.connect()
#             dce = rpc_con.get_dce_rpc()
#             dce.connect()

#             print(dce.get_auth_type())
#             print(dce.get_session_key())

#             dce.bind(samr.MSRPC_UUID_SAMR)
#             resp = samr.hSamrConnect(dce)

#             resp2 = samr.hSamrLookupDomainInSamServer(dce, resp['ServerHandle'], 'DOMAIN_NAME')
#             domain_handle = resp2['DomainHandle']

#             resp3 = samr.hSamrQueryInformationDomain(dce, domain_handle, samr.DOMAIN_INFORMATION_CLASS.DomainFullInformation)
#             print('FQDN:', resp3['Buffer']['DnsDomainName'])

#         except Exception as e:
#             print(f"Error: {e}")
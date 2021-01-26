# Notes regarding Vagrand and Odin environemnts

ne vezano za ovo - za linux konekciju probati No Machine

hosting is not used any more / rarely
billing is the most important part

machines:
  manager
  billing
  billing_db
  billing_store
  proxy
  gateway/ui

Procedure:
spin 6 machines from awx
templates, 
provision  VM, 
start 6 machines / each one needs to be strated individually
in inventory add new inventory, add hosts
run template to add users to desired inventory

once management machine is up and running
run update
log on to management node and add other nodes


once logged in
informatin - licenses add license
modules
add billing module
This needs to be checked in tasks - here it will show status of this job
infrastructure - service nodes - add machines
When installing new node add backnet ip with root credentials
license must be added to the billing node as wel
order to add
1. applicaton
2. db
3. online store
4. ui
5. endpoint

Networking
All machines have two networks - frontNet and backNet
Default `eth0` network must be deleted, that must be done directly via VirtualBox, not `ssh`
Commands for this are in the guide

Adding nodes:
BN *( application )
  module must be added first in infrastructure/package/modules
  specify backnet ip
  BSS application: BN frontnet ip
  BSS DB: DB backnet IP
  enable optional parameters
  add root username and password
  set proper frontent and backent IPs
  go to IP of this server https://<ip>:8443 login and add license
    add ZIP code details and related stuff (NY, USD...)
    products/online store/connection setup
    edit: store backnet IP, https, 443
    sync now
DB
  was added within the first step
OnlineStore
  just specify frontent and backnet ip
UI
  just specify frontent and backnet ip
  once it is installed add UIip on DBapp node (check in wiki)
Endpoint
  just specify frontent and backnet ip
domain_SDK (node added manually)
  just specify frontent and backnet ip
  
# OPENVPN

Go to openvpn web ui
User_permissions
Create new user, must exist in AD 
set rules based on some other user e.g Nokia


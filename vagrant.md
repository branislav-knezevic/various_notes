# Installation gude for Odin

ne vezano za ovo - za linux konekciju probati No Machine

hosting is not used any more / rarely
billing is the most important part

machines:
- management
- billing
- billing_db
- billing_store
- proxy
- gateway/ui

## Old Vagrant procedure:

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
0. management
1. applicaton / billing
2. db
3. online store
4. ui
5. endpoint
6. DNS


## Networking

All machines except MN have two network adapters - frontent and backnet. 
On MN only backet on `eth0` which has a gateway and DNS
On all other machines `eth0` is backnet without gateway and DNS, while frontent `eth1` has both of them configured


## Adding nodes:

### MN (management node)

Official online guide:
https://docs.cloudblue.com/cbc/20.5/premium/content/Linux-Platform-Deployment-Guide/Installing-Linux-based-Product-Management-Node.htm

How installation is done in Devtech:
obtain installation package, check with Steva from where or copy from one of the exising machines, usually it is located in `/arhiva`
Installations are located on vagrant share (needs to be checked how it should be copied here)
directory
for copy use `rsync` command
`rsync` is used to copy files via ssh between multiple systems
run this from your MN server
`rsync -zarvh <user>@<ip>:<path_to_file_on_remote> <path_on_local>`
eg:  
`rsync -zarvh root@192.168.71.64:/arhiva/dist-20.5.tar /arhiva`
go to `/arhiva` and untar the installation
`tar xvf dist-20.5.tar`
go into extracted direcotry and run:
`python install.py --batch --modules="Platform,APS" --password "admin"`

Once Installation is complete, go to browser and log in to `http://<mn_backnet_ip>:8080` with creds admin/admin
In Keeper locate a valid license and downlaod
Unzip if needed and upload to  System > Information > Product License

Once that is done, go to ssh console again and install updates via:
`oa-update --install`

### BN ( application )

module must be added first in infrastructure/package/modules
specify backnet ip
BSS application: BN frontnet ip
BSS DB: DB backnet IP
enable optional parameters
add root username and password
set proper frontent and backent IPs
go to IP of this server https://<ip>:8443 login and add license
- add ZIP code details and related stuff (NY, USD...)
- products/online store/connection setup
- edit: store backnet IP, https, 443
- sync now

### DB

was added within the first step

### OnlineStore

just specify frontent and backnet ip

### UI

just specify frontent and backnet ip
once it is installed add UIip on DBapp node (check in wiki)
on the Billing App/BSS node do the following:
append the Branding/UI frontnet interface IP address to the `/usr/local/bm/conf/ip_access.db` and restart pba service
`echo '<UI_frontnet_ip> = true' >> /usr/local/bm/conf/ip_access.db`
`service pba restart`

### Endpoint

just specify frontent and backnet ip

### domain_SDK (node added manually)

just specify frontent and backnet ip
  
# OPENVPN

Go to openvpn web ui
User_permissions
Create new user, must exist in AD 
set rules based on some other user e.g Nokia


# Manual machine configuration

If servers have not been installed via AWS and hence cofigure, they need to be configured manually
Each machine must have 2 network adapters - one for frontnet and one for backnet
In machine configuration, both network adapters need to be configured
```
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```
In it edit IP to a desired one.
For second adapter do:
```
cp /etc/sysconfig/network-scripts/ifcfg-eth0 /etc/sysconfig/network-scripts/ifcfg-eth1
vi /etc/sysconfig/network-scripts/ifcfg-eth1
```
Change UUID, update network to match backnet IP and delete default gateway and DNS  
Once this is configured network service needs to be restarted via:
```
sudo systemctl restart network
```

Each machin must be accessible via root user or some other regular user with root privileges
This is done via `vim /etc/ssh/sshd_config`
Make sure to have the following lines set like this:
```
PermitRootLogin yes
PermitPasswordAuthentication yes
```
Hostname for each machine must be changed to `<role>.<domain` and this can be done via command `hostnamectl
set-hostname <hostname>`
e.g.: `hostnamectl set-hostname mn.spamexperts.devtech.rs`
An entry must be added to each machines hosts file (`/etc/hosts`) which contains a backnet IP of BN node
e.g.: `192.168.72.65 bn bn.spamexperts.devtech.rs`
Following commands must be initiated on each server:
`yum clean all && yum update -y`
`yum -y install kernel kernel-devel gcc binutils make perl bzip2`
Only on endpoint node, some extra stuff needs to be installed:
```
sudo yum -y install mod_ssl epel-release
sudo yum -y install https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
sudo yum -y install php56w* --skip-broken
sudo yum -y install https://download.automation.odin.com/aps/php.runtime/aps-php-runtime-8.0-121.el7.noarch.rpm
sudo systemctl enable httpd
sudo systemctl start httpd
```
Once this is all complete make a snapshot of all of them

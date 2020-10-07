# Procedure how to create machines via AWX

Connect to hypervisors manually to check the availability of CPU RAM and HDD

Templates > Provision VM (click on rocket on the right hand side)

Name, host...
IP addres choose from available internal IPs on resources document, exclude it from there
Add this IP with necessary details in the same dock on `ldex uk vms on hypervisors` tab
Adjust gateway to match the IP range of the machine 88/87 
Not sure what for or if password is used

Once machine is done, go to `Inventories`
Select desired inventory and copy it (button on the right)
Rename it to some friendly name, it can match a VM
Hit `Save`
Go to hosts, delete the exising on and in the `HOST NAME` field type in the IP 

Go back to templates
Locate some user management template, make a copy, change the name and adjust the users which need to access that
machine
Make sure to change the desired destination in Inventory field
Hit save and then launch


For windows machine
set inventory as above
go to templates - `after provisioning windows`, add proper inventory
Use `workflow - provison Windows VM`


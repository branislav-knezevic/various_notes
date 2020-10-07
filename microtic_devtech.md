# Microtic Devtech instructions

## Connecting to the device

To connect to microtic locate record in keeper `UK Mikrotik coreldex`
SSH into it with credentias found in that record

## General

`tab` shows the current available commands

## Setting up nat

To set up NAT go to
`ip`
`firewall`
`nat`

Command `print` prints all current routes.
Scroll down with pres of the `space bar`
Routes which are disabled are marked with *****X** at the beggining

```
18 X  ;;; Exchange 2010SP1 multy-tenant
      chain=dstnat action=dst-nat to-addresses=192.168.88.243 protocol=tcp dst-address=37.220.108.85 in-interface=WAN log=no log-prefix=""
```  

Command `export` shows the list of created rules  
Adding rule example:
```
add action=dst-nat chain=dstnat comment="Acronis Kaseya Kubernetes - Branislav Knezevic" dst-address=37.220.108.93 dst-port=18443 protocol=tcp in-interface=WAN to-addresses=192.168.87.34 to-ports=443
```
Existing rules can be edited with `edit` command
`edit`
Enter the number of the rule which can be obtaind from the `print` command
`<value-name>`
It will open a text editor in which the value will need to be edited

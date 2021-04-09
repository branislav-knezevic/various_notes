# Terraform notes

`terraform state list` shows all available terraform state files
`terraform state show <state_file_name` opens specific terraform state file




### Old notes
When variables are used, they have to be in all layers (main + module)
	in module they are specified as empty
		variable "name" {}
	in main variable would be specified
		name = "photocardservice"
		
practice

create simple AWS infrasturucture
Create files with pub_key for easy access

set variable `TF_LOG=1` to enable logging
`terraform plan|apply -var "<terraform_var_name>=${VAR_NAME}"` supply additional variables which are not defined in cofig files

## Workspaces

Workspaces are used when same configuration needs to be applied to multiple environments
Only workspace is the `default` one and it can't be deleted

`${terraform.workspace}` is used as variable in terraform code
`terraform workspace new <workspace_name>` creates a desired workspace
`terraform workspace select <workspace_name>` selects that workspace

How infrastructure should look like by Gruntworks:
Infrastructure
  dev
	  vpc
		mysql
		servers
  staging
	  vpc
		mysql
		servers
  prod
	  vpc
		mysql
		servers
	Modules these modules can call some other smaller modules
	  vpc
		mysql
		server_related

Checkout terratest and cloud-nuke, both by Gruntworks

## Explaining some functions

### for_each and if

```
for_each = var.create ? var.zones : tomap({})

variable "create" {

  description = "Whether to create Route53 zone"
  type        = bool
  default     = true
}

variable "zones" {
  description = "Map of Route53 zone parameters"
  type        = any
  default     = {}
}
```

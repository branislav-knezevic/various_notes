resource "aws_route53_zone" "this" {
  # for each entry which has create set to true use zones record
  for_each = var.create ? var.zones : tomap({})

  # use key of the zone which is some_zone.local as a name
  name = each.key

  # go throuth the values of zones key which are maps (comment, tags, vpc_id...) 
  # locate the one who's key matches comment and use it's value
  # otherwse set value to null
  comment = lookup(each.value, "comment", null)

  # same as for comment, just with value "force_destroy"
  force_destroy = lookup(each.value, "force_destroy", false)

  # `dynamic` and `for_each` always go together
  # Check if there is a map named vpc with `try`
  # Look in vpc map for any value which contains vpc and convert it to list if it isn't a list already
  dynamic "vpc" {
    for_each = try(tolist(lookup(each.value, "vpc", [])), [lookup(each.value, "vpc", {})])

    content {
      vpc_id     = vpc.value.vpc_id
      vpc_region = lookup(vpc.value, "vpc_region", null)
    }
  }

  tags = merge(
    lookup(each.value, "tags", {}),
    var.tags
  )
}

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

variable "tags" {
  description = "Tags added to all zones. Will take precedence over tags from the 'zones' variable"
  type        = map(any)
  default     = {}
}


inputs = {
  zones = {
    "some_zone.local" = {
      comment = "DNS zone for test project in dev environment"
      vpc = {
        vpc_id     = ""
        vpc_region = ""
      }
      tags = {}
    }
  }
}

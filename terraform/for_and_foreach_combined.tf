locals {
  envs = [{
    name = "management"
    data = data.terraform_remote_state.mgmt-vpc.outputs.private_subnet_cidr,
    }, {
    name = "develop"
    data = data.terraform_remote_state.develop-vpc.outputs.private_subnet_cidr,
    }, {
    name = "test"
    data = data.terraform_remote_state.test-vpc.outputs.private_subnet_cidr,
    }, {
    name = "uat"
    data = data.terraform_remote_state.uat-vpc.outputs.private_subnet_cidr,
    }, {
    name = "stage"
    data = data.terraform_remote_state.stage-vpc.outputs.private_subnet_cidr,
    }, {
    name = "production"
    data = data.terraform_remote_state.production-vpc.outputs.private_subnet_cidr
  }]
}

# VPC

resource "aws_security_group" "alb_sg" {
  name        = "${local.service_name}-alb-security-group"
  description = "Security group for Unleash server LB with access to proxy"
  vpc_id      = data.terraform_remote_state.mgmt-vpc.outputs.vpc_id
  tags        = local.tags

  dynamic "ingress" {
    for_each = local.envs
    content {
      description = "access to ${local.service_name} LB from ${ingress.value.name} subnets"
      from_port   = 80
      to_port     = 80
      protocol    = "tcp"
      cidr_blocks = [
        for cidr_value in ingress.value.data : cidr_value
      ]
    }
  }
  dynamic "ingress" {
    for_each = local.envs
    content {
      description = "access to ${local.service_name} LB from ${ingress.value.name} subnets"
      from_port   = 8080
      to_port     = 8080
      protocol    = "tcp"
      cidr_blocks = [
        for cidr_value in ingress.value.data : cidr_value
      ]
    }
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


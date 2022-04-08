# EKS

AWS controls the control plane (master nodes)

## Usefull tools

`eksctl` not aws tool, can be used to simply create cluster
it may be used for local setup?

## 5 tenets - principals

Source: 
https://www.youtube.com/watch?v=cipDJwDWWbY&t=5s

### Security

Encrypt secrets with KMS or
store secrets in Secrets manager - use Secrets Manager CSI driver to obtain
Use ACM to generate certificates - use cert manager plugin

ETCD volumes are managed by EKS and they are already encrypted

Enable only the private endpoint (access via bastion or VPN)

Recommendation is to use OS optimized for containers - eg Bottlerocket
New version - new AMI

Don't enable SSH, use Systems manager

#### Security at Pod level

Using IAM accounts for service account - IRSA
Create role, assing to k8s account and namespace and cluster
Pod then requires additional annotation to pick up this role

Optional - restrict pod access to metadata - IMDS

Pods can be associated to specific security group
eg. only specific nodes need access to RDS

#### Additional best practices

- use namespaces and RBAC
- set quotas and limits to restrict resources usage
- API priority and Fairness???
- enforce polices to limit what can be run in the cluster
- deny cross namespace traffic via network policies

### Reliability

AWS manages ETCD accross 3 AZs
Upgrades are done in a rolling mode
Automated ETCD backups

Our responsibility to monitor (Prometheus)
Vizualize metrics in Grafana
Enable control plane audit logging

### Efficiency

Scale pods h/v based on usage (close to actual utilization)
Horizonal Pod Autoscaling - HPA
Vertical Pod Autoscaling - VPA

Scale node resource based on pod requirements
Monitor for pending pods and autoscale if needed
explore Karpenter - for autoscaling in large clusters with fast scaling requirements 

### Cost reduction

Spot instances with managed node groups
cluster autoscaler priority expander to prioritize lower cost node groups
savings plan for EC2
Latest gen EC2
move workloads to EC2 Graviton - if compute is needed

### Cluster operations

Recommendation is to run cluster per env
Upgrade - should be failry simple, single API call
2-3 times per year do an upgrade
do an upgrade in test first (of course)

### User access

Authentication:
- IAM is an option
- OpenID Connect - integrate some other existing identity management
Authorization:
- k8s RBAC

### Monitoring

Control Plane side
- enable control plane logging
- collect and monitor control plane Prometheus metrics for API request latency
- run kube-state-metrics
Application side
- OpenTelemetry ???
- Logging - AWS Distro for Fluent Bit

### Traffic routing

AWS LB - ingress --> ALB

### Deploying

GitOps - store configuratoin/manifest in a repo

------

# Usefull tools and guides

gruntwork guides
https://blog.gruntwork.io/comprehensive-guide-to-eks-worker-nodes-94e241092cbe

autoscale cluster if using node-groups
https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler






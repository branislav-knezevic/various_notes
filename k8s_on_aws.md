# Setting up k8s cluster on amazon AMI

install desired number of instances  
set SG to allow all traffic on internal network network  
create custom policy:  
```
{
    "Version": "2012-10-17",
    "Statement": [
	{
	    "Effect": "Allow",
	    "Action": [
		"ec2:CreateRoute",
		"ec2:DeleteRoute",
		"ec2:ReplaceRoute"
	    ],
	    "Resource": [
		"*"
	    ]
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"ec2:DescribeRouteTables",
		"ec2:DescribeInstances"
	    ],
	    "Resource": "*"
	}
    ]
}
```
create new role and attach this new policy  
maybe attach these roles as well # probably not needed  
    EC2 full
    IAM full
    S3 full
    Route53
on all nodes  
    add repo
	cat <<EOF > /etc/yum.repos.d/kubernetes.repo
	[kubernetes]
	name=Kubernetes
	baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
	enabled=1
	gpgcheck=1
	repo_gpgcheck=1
	gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
	EOF
    Install these programs
	sudo yum install -y kubectl kubelet kubeadm docker
    run following as regular user
	mkdir -p $HOME/.kube
	sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
	sudo chown $(id -u):$(id -g) $HOME/.kube/config
Only on master
    for using cluster with Flannel network run:
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16
    kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
On slaves
    kubectl join command supplied after kubeadm init was ran



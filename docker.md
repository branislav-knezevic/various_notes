#---------------#
#				#				
#  D O C K E R  #
#				#
#---------------#

	--- General ---

docker info # basic info 
docker version # info about server and docker version
Namespaces:
	Each containter has its own
		Process ID (pid) # each container has it's own isolated process tree
		Network (net) # it's own isolated network stack 
		Filesystem/mount (mnt) # it's own root drive / or c:\
		Inter-proc comms (ipc) # allows processes within the container to access same shared memory
		UTS (uts) # every container gets it's own hostname
		User (user) # allows mapping from container users to host OS users
Control Groups (Job Objects in Windows) # resource control per container

docker login devtechregistry.azurecr.io -u <keeper> -p <keeper>

	
-------------------------------------------------------------

	--- Docker containers ---
	
docker ps # list running containers
docker ps -a # list containers with history
docker start [container name]
docker stop [container name]
docker rm [container name] # remove specific container
docker run [image name] # start new container from specific image
	docker run hellow-world
	docker run -d --name web -p 80:8080 something/something
	# start container from image something/something in the background (-d) with a name web and map port 80 on host to 8080 in the container
	# this container will be pingable via name if it is on the same network as some other container
	docker run -it --name temp ubuntu:latest /bin/bash
	# run a docker container named temp in interactive session (-it) and run /bin/bash process in it
docker stop $(docker ps -aq) # stop all containers that are returned by docker ps -aq (q for quiet)
docker container run --isolation=hyperv # only on Windows to run a hypervized container with linux
docker container run -it [image-name] sh # sh is shell process 
docker container exec -it [container-name] [process] # e.g. sh process
docker container exec [container-name] [command] [file-name] # will execute commands on files from the container
	docker container exec cont1 cat textFile # will output content of the text file-name
docker port [container-name] # shows list of mapped ports
docker logs [container-name] # view container logs for specific container

  -- build a container --

In the same working directory where the app code is create Dockerfile (Capital D!!!)
INSTRUCTION value # CAPITALIZE instructions
Content (without quotes):
'FROM' base image # Layer 1
	FROM centos
'LABEL' maintainer="branislav.knezevic@live.com" # just metadata
'RUN' command which needs to run # Layer 2
	RUN yum install httpd
'COPY' copy code from where to desired directory on the image # Layer 3
	COPY /docker /var/www/html
'WORKDIR' path to directory # just metadata for working directory
	WORKDIR /var/www/html
'RUN' some more content if needed # Layer 4
	
'EXPOSE' port number # metadata
	EXPOSE 8080
'ENTRYPOINT' run the app (relative to WORKDIR) # metadata
	ENTRYPOINT service httpd start 

Docker image build -t [image-name] [path-to-files]
	docker image build -t webserver /docker
	
	-- logs --

Daemon logs:
	systemd
		journalctl -u docker.service
	non-systemd
		/var/log/messages
	Windows
		~/AppData/Local/Docker
Container logs
	docker logs [container-name]
	
komanda za pracenje docker logova docker-compose logs -f --tail=50



------------------------------------------------------------------------
	
	--- Docker images ---

/var/lib/docker/ # location of image files on linux
registry/repo/image(tag) # if registry and image are not specified, default is docker hub as registry and latest as image
	docker.io/redis/latest # if image has "latest" tag - it doesn't mean that it has to be the latest. That tag is added manually
images and layers in registry are marked with a distribution hashes (compressed content hashes with a manifest file)
images and layers on host are marked with a content hashes. Those two are not the same
when image is pulled locally it uses content hash and while it is in the registry the distribution hash
docker images # lists available images on the server
docker pull [image name] # download image without running it
docker pull [image name]:[version] # specific version of image
	docker pull ubuntu:14.04
docker rmi [image name]:[version/tag] # remove image from server
docker rmi [image id] # same thing
docker rmi $(docker images -q) # same as for containers
docker history [image name] # history of commands on which image was built
docker image inspect [image name] # more detail insight in JSON format
docker image ls --digests # also more detail insight
docker tag [source-image] [target-image]:[tag]
	docker tag 14f96ec6c738 centos:latest # tags image into centos:latest

------------------------------------------------------------------------
	
	--- Docker Swarms ---
	
# A Swarm = a cluster
# Engines in a swarm run in swarm mode
# Swarm consists of one or more Worker and Manager nodes
# 	Manager nodes maintain the swarm (3-5 recomended, must be an odd number, only one is a leader)
# 	Worker nodes execute tasks (managres are also workers)
# Services - only available in swarm mode
# 	declarative way of running and scaling tasks (containters)
# 	services are split into tasks
# Tasks - atomic unit of work assigned to a worker node - containers with metadato how to initiate a container

docker swarm init --advertise-addr [IP-address]:2377 --listen-addr [IP-address]:2377
	swarm init # start swarm
	--advertise-addr # use this ip and port an IP for this swarm node
		2377 # swarm port
		2376 # secure engine port
		2375 # engine port
	--listen-addr
docker swarm join-token [manager/worker] # obtain a command with tocken to add worker/manager to swarm
docker node ls # lists all available nodes - available only on master nodes
docker node promote [container-ID] # promote worker to manager
docker service create --name [service-name] -p 8080:8080 --replicas 5 [imagelocation/name]
	docker service create # create docker service
	--name # name of the service which is running
	-p # map specific ports
	--replicas # desired number of replicas
	imagelocation/name # which docker image to use for this service
docker service ls # list of all running services
docker service ps [service-name] # info about the service
docker service inspect [service-name] # more detail info
	--pretty # can be added  for more friendly output
docker service scale [service-name]=[number] # update number of replicas
docker service update --replicas [number] [service-name] # this would do the same thing
docker service rm [service-name] # remove service
docker service update --image [imagelocation/name]:[version] --update-parallelism 2 --update-delay 10s [service-name]
	--update-parallelism # how many tasks to update at once
	--update-delay # how much to wait before updating the next bunch
docker swarm join-token --rotate [manager/worker] # create new token 
sudo openssl x509 -in /var/lib/docker/swarm/certificates/swarm-node.crt -text # get certificate used in swarm
	Subject: O=g99te1gz4gf618ztow7u6xwab, OU=swarm-manager, CN=ovxln4nk7hagtvmm5fzp4deff
		O=g99te1gz4gf618ztow7u6xwab		# swarm id
		OU=swarm-manager				# node role
		CN=ovxln4nk7hagtvmm5fzp4deff	# node id
Locking the swarm # prevents restarted Managers from automatically re-joining the Swarm and prevents accidentally restoring old copies of the Swarm
docker swarm init --autolock # autolock new swarm
docker swarm update --autolock=true # autolock existing swarm. make sure to copy the given key as only with it it will be able to re-join the swarm
	key example: SWMKEY-1-rcOBCjAe0eLdHzDg3NwP+xJhBDryQHa2Q8MRSZj09d4
	
------------------------------------------------------------------------------------------------------

	--- Network ---

Bridge Networking (NAT)  
	most commonly used
	containers on different hosts can''t talk to each other
	only way to get to the internet is port mapping
Overlay (Multihost) Networking
	single L2 network spanning multiple hosts
	new virtual network is created and containers are then joined to it
	used only to enable containers to talk to each other
MACVLAN (transperent driver on Windows)
	all containers get their IP and MAC
	must allow promiscous mode on the host NIC # cloud providers generally don't allow that
IPVLAN
	Similar to MACVLAN
	Containers get their IP but NOT MAC
	More cloud friendly
	May have problems with DHCP as they distribute IPs per MACs
	Containers can''t ping their hosts

docker network ls # lists all available networks
	# scope 
		# local - single-host
		# swarm - mulit-host
docker network inspect brigde # more details on bridge adapter
docker network inspect nat # same thing on windows
docker network inspect [adapter-name] # more info on specific adapter
docker network create -d [driver-name] [network-name] # creates new bridge network with specified name. Driver bridge/overlay
	docker network create -d bridge --subnet 10.0.0.1/24 ps-bridge
	# user made docker overlay network will only appear on other swarm members when node which has this nettwork attached is created on them
	# built in ingress overlay network will be available instantly
	# if there are any published ports, those services also get attached to ingress network by default
yum install bridge-utils
brctl show # lists all bridged networks
	# usally will show docker0 bridgde which is a default one if none other are specified, that is the 
	# default one which is installed with docker. If any additional are created, they have a different name
	

Network Services
	Service Discovery # locate services in a swarm
	Load Balancing # allows to access the service on any node in a swarm, even though it is not even hosting the service
When two services are created on the same overlay network they are pingable by name because of swarm DNS
Three pillars of docker networking
	Container Network Model (CNM) # specification document hosted on github https://github.com/docker/libnetwork/blob/master/docs/design.md
		Container Network Interface (CNI) # exits, works with Cubernetes and CNM works with Docker
		Sandbox # namespace - isolated area on OS which can be tweeked without affecting the system
		Endpoint # network interfaces
		Network # bunch of endopints which can talk to each other
	Libnetwork # real world implementation of the CNM, written in Golang
	Drivers # on top of the network
			# different types of drivers for different types of networks
		Local drivers # native, come with docker
		remote drivers # third-party drivers
When service is created it gets its own IP (VIP) and each container within it gets its own IP as well (from the same subnet). 
Requests are sent to IP of the service and then round-robined to healthy containers
Routing Mesh # when requests are forwarded even from nodes which don't host any nodes
HTTP Routing Mesh (HRM) # Requires Docker Datacenter
	HRM needs to be enabled manually
	Allows forwarding of multiple apps/sites on the same port
		
------------------------------------------------------------------------------------------------------

	--- Volumes ---
	
Like shared drives between containers.
Persistent storage unlike container storage which is ephimeral
Default location
	/var/lib/docker/volumes

docker volume create [volume-name]
docker volume ls...
docker volume inspect...
docker volume rm ...
docker container run -dit --name [container-name] --mount source=[volume-name],target=[path] [image-name]:[version] # run a container and mount volume on specific directory
	docker container run -dit --name voltest --mount source=bkvolume,target=/vol alpine:latest
	
------------------------------------------------------------------------------------------------------

	--- Stacks ---
	
Stack document:
	version
	services
	networks
	volumes

docker stack create -c [yaml-file] [stack-name] # create stack from specified yaml file 
docker stack ls/ps/rm
docker stack services [stack-name] # similar as docker stack ps [stack-name]
after YAML file is updated, command docker stack create -c [yaml-file] [stack-name] need to be run again
	
------------------------------------------------------------------------------------------------------

## docker-compose

Yaml file, contains full config for one or multiple docker containers 
File should be named `docker-compose.yml` (or `yaml`)
`docker-compose up` starts all containers which are defined within a file. Needs to be triggered from the directory
where `docker-compse.yml` file is located
`docker-compose -f <path_to_file>` if config file is located else where
`docker-compse -d up` will start all services in detached mode, otherwise it will show logs and current terminal will be
locked by it
`docker-compse -d <service_name>` starts specific service from the config file
`docker-compose stop <service_name>` stops specific service from the config file
`docker-compose down` stops and shuts down all services

			


		
	

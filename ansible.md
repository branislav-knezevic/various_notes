# Ansible Notes

## Ansible general

`ansible-doc` internal documentation
`ansible-doc -l` list of all available modules, may be outputed into a file with > <file_name>
`ansible-doc ec2` help for a specific module
`/etc/ansible` default ansible instalation dir, contains examples of ansible.cfg and hosts file.
 this ansible.cfg file is usefull ans it contains a lot of examplas of things which can be configured in this file



## Ansible commands

all are ran as ansilble ...
--list-hosts all # list all hosts in ansible hosts file
	"*" # does the same thing
	<group_name> # for specific group
	<host_name> # for single host
	"host_n*" # with asterisk
	<group1>:<group2> # specifying multiple groups
	<group1>,<group2> # same thing
	<group_name>[<number>] # host with specific order number 0,1...
	\!<group_name> # everything apart from
		"" and \ are used only in bash
	# file location /etc/ansible/hosts
	# custom hosts file can be made and app pointed to it with -i parameter
	# in custom hosts file, for the entry of the control add ansible_connection=local
	  # so it would not try to connect to it via standard ssh
		ansible -i <custom_hosts_file> --list-hosts all
	# location of hosts file can be changed in /etc/ansible/ansible.cfg, inventory line
	# or new ansible.cfg file with custom values can be created and ansible can be run from the same directory where this file is
`-m ping all` ping all hosts, -m is for module
`-m command -a "hostname" all` send hostname command to all hosts
`-m` command is a default
`-a "hostname" all` would do the same thing
`"on docs.ansible.com"` list of all modules
`ansible -m setup <host_name>` it executes just gathering facts step
`ansible-playbook database.yml -e db_name=myapp...` variable passed via command line
`ansible-vault create <vault_filename>` do this within a folder where you want it
`ansible-vault edit <vault_filename>` to change the content after it has been saved
then point the unencrypted variable to the encyrpted one
when running a playbok which contains a encrypted pass
`ansible-playbook --ask-vault-pass`
or store this pass in a file outside of a folders which are pushed to a repo as plain text
this can be done each time via command line
`ansible-playbook --vault-password-file <path_to_file>`
or better put it into ansible.cfg as
`vault_password_file = <path_to_file>`
`ansible-playbook site.yml --limit app01` limits a specific host but applies all rules from site.yml
each task or role can be tagged
`ansible-playbook site.yml --tags "<tag_name>"` executes only tasks which are marked with that tag
`ansible-playbook site.yml --skip-tags "<tag_name>"` same thing to skip ceertain tasks
it helps to mark all steps which install packeges to be skipped, speeds things up

`ansible-playbook site.yml --step` asks for each step should it be executed
`ansible-playbook site.yml --list-tasks` shows all tasks
`ansible-playbook site.yml --start-at-task "<task_name>"` start specific task
`ansible-playbook site.yml --limit @/path_to_file.retry` retries only failed hosts
`ansible-playbook --syntax-check site.yml` just checks syntax
`ansible-playbook --check site.yml` dry run, preview of things that will be done



### playbooks ###

saved as .yml file
simple playbook:
```
---
  - hosts: all # on which hosts to execute
    tasks: # which commands
      - name: get server hostname # optional name of this step
	command: hostname # which bash command to execute
```
`ansible-playbook <path_to_playbook_yml>` run a specific playbook
whan playbook is ran, there are three steps
`GATHERING FACTS` gathering basic info about hosts and returning it to playbook
`TASK` executing specified commands
`PLAY RECAP` summary of executed commands

4 pillars for most linux apps
  1. required packages # download deb...
  2. service handler/tracker # upstart nnd, systemd... tracking service status
  3. system configuration # required files, dirs, users, permissions, iptables...
  4. config files for the app


### playbooks from lecture 

loadbalancer
```
---
- hosts: loadbalancer
  become: true # run tasks as sudo
  tasks:
    - name: install tools
      apt: name={{item}} state=present update_cache=yes
      with_items:
        - python-httplib2

    - name: install nginx
      apt: name=nginx state=present update_cache=yes
      # name is name of the apt package
      # state is which version,
        # present - is current, latest but just this time
        # latest - will always install the latest
        # exact version can be specified as well
        # absent - remove the package if it is installed
      # update_cache # apt get update
      async: 300 # makes this job run in parallel on all specified hosts, number is the maximum time for which ansible will wait for this command to complete
      pole: 3 # time in seconds, ansible will check every 3 seconds if this task has been completed on all hosts

    - name: configure nginx site
      template: src=templates/nginx.conf.j2 dest=/etc/nginx/sites-available/demo mode=0644
      # templates file is pulled from the control machine, in this case it contains a loop for going
        # through servers and adding them to the list, variable <groups> from conf file  is used
      notify: restart nginx

    - name: get active sites
      shell: ls -1 /etc/nginx/sites-enabled
      # run a bash script, -1 mens one per line
      register: active # register result within variable "active"

    - name: de-activate sites
      file: path=/etc/nginx/sites-enabled/{{ item }} state=absent
      with_items: "{{active.stdout_lines}}"
      when: item not in sites
      # go through lines in active variable and remove ones which don't macth the vlaue
        # from sites item in dictionary (myapp)
      notify: restart nginx

    - name: activate demo nginx sites-enabled
      file: src=/etc/nginx/sites-available/demo dest=/etc/nginx/sites-enabled/demo state=link
      notify: restart nginx

    - name: ensure nginx started
      service: name=nginx state=started enabled=yes
      # name - name of the desired service
      # state - should it be automatically started
        # started/restated/stopped/reload
      # enabled - should it be started automatically

  handlers:
    - name: restart nginx
      service: name=nginx state=restarted
```
database
```
---
- hosts: database
  become: true
  tasks:
    - name: install tools
      apt: name={{item}} state=present update_cache=yes
      with_items:
        - python-mysqldb

    - name: install mysql-server
      apt: name=mysql-server state=present update_cache=yes

    - name: ensure mysql listening on all ports
      lineinfile: dest=/etc/mysql/my.cnf regexp=^bind-address
                  line="bind-address = 0.0.0.0"
      # locate a specific line which is determined by regular expression and replace it with a value of line=""
      notify: restart mysql

    - name: make sure mysql started
      service: name=mysql state=started enabled=yes

    - name: create demo database
      mysql_db: name=demo state=present

    - name: create demo user
      mysql_user: name=demo password=demo priv=demo.*:ALL host='%' state=present


  handlers:
    - name: restart mysql
      service: name=mysql state=restarted
```

webserver
```
---
- hosts: webserver
  become: true
  tasks:
    - name: install web components
      apt: name={{item}} state=present update_cache=yes
      # or name: ['apache2', 'libapache2-mod-wsgi', ...]
      # {{item}} runs a for each for the items below
      with_items:
        - apache2
        - libapache2-mod-wsgi
        - python-pip
        - python-virtualenv
        - python-mysqldb

    - name: ensure apache2 started
      service: name=apache2 state=started enabled=yes

    - name: ensure mod_wsgi enabled
      apache2_module: state=present name=wsgi
      notify: restart apache2 # name of the handler
      # state present will enable module in apache
      # if there are multiple notifications which do the same thing they will wait until the end
      # and then that task will be done only once, not after every notification
    - name: copy demo app source
      copy: src=demo/app/ dest=/var/www/demo mode=0755
      # if it is a relative path in src file has to be where the yml file is
      # if src ends with / it means that it will copy that folder with all of it contents
      # without / it would copy only the content
      notify: restart apache2

    - name: copy apache virtual host config
      copy: src=demo/demo.conf dest=/etc/apache2/sites-available mode=0755
      notify: restart apache2

    - name: setup python virtualenv
      pip: requirements=/var/www/demo/requirements.txt virtualenv=/var/www/demo/.venv
      # pip installs prerequisites for python applications which can be listed in requirements.txt
      notify: restart apache2

    - name: de-activate default apache site
      file: path=/etc/apache2/sites-enabled/000-default.conf state=absent
      # file is used to modify file properties directly on the target
      # this command tells to locate the desired file and delete it
      notify: restart apache2

    - name: activate demo apache site
      file: src=/etc/apache2/sites-available/demo.conf dest=/etc/apache2/sites-enabled/demo.conf state=link
      # state link means to actually create a link
      # state present would crate an actual file
      notify: restart apache2

  handlers:
    - name: restart apache2
      service: name=apache2 state=restarted
      # this handler doesnt automatically restart the service, it needs a trigger
```

control
```
---
- hosts: control
  become: true
  tasks:
    - name: install tools
      apt: name={{}} state=present update_cache=yes
      with_items:
        - curl
        - python-httplib2
```

stack restart
```
---
# bring stack down
- hosts: loadbalancer
  become: true
  tasks:
    - service: name=nginx state=stopped
    - wait_for: port=80 state=drained
    # wait for checks if the service is stopped and
    # state=drained that all existing connectiones are dropped

- hosts: webserver
  become: true
  tasks:
    - service: name=apache2 state=stopped
    - wait_for: port=80 state=stopped

# restart mysql
- hosts: database
  become: true
  tasks:
    - service: name=mysql state=restarted
    - wait_for: port=3306 state=started

# bring stack back up
- hosts: loadbalancer
  become: true
  tasks
    - service: name=nginx state=started
    - wait_for: port=80

- hosts: webserver
  become: true
  tasks:
    - service: name=apache2 state:started
    - wait_for: port=3306
```

service-status-check
```
---
- hosts: loadbalancer
  become: true
  tasks:
    - name: verify nginx service
      command: service nginx status

    - name: verify nginx is listening on 80
      wait_for: port=80 timeout=1
      # by default timeout is 100 seconds

- hosts: webserver
  become: true
  tasks:
    - name: verify apache2 service
      command: service apache2 status

    - name: verify apache2 is listening on 80
      wait_for: port=80 timeout=1

- hosts: database
  become: true
  tasks:
    - name: verify mysql service
      command: service mysql status

    - name: verify mysql is listening on 3306
      wait_for: host={{ ansible_eth0.ipv4.address }} port=3306 timeout=1
      # host={{ ansible_eth0.ipv4.address }} was added after it was changed later in roles
      # at first this was done without the host= part

- hosts: control
  tasks:
    - name: verify end-to-end response
      uri: url=http://{{item}} return_content=yes
      with_items: "{{groups.loadbalancer}}"
      # loop is used in case more loadbalancers are added,
      register: lb_index
      # creates new variable lb_index with the content of uri check

    - fail: msg="index failed to return content"
      when: "'Hello, from sunny' not in item.content"
      # in this chase it is Hello, from sunny
      with_items: "{{lb_index.results}}"
      # this loop is because of the with_items from the previous step

    - name: verify end-to-end db response
      uri: url=http://{{item}}/db return_content=yes
      with_items: "{{groups.loadbalancer}}"
      register: lb_db

    - fail: msg="db failed to return content"
      when: "'Database Connected from' not in item.content"
      with_items: "{{lb_db.results}}"

- hosts: loadbalancer
  tasks:
    - name: verify backend response
      uri: url=http://{{item}} return_content=yes
      with_items: "{{groups.webserver}}"
      register: app_index

    - fail: msg="index failed to return content"
      when: "'Hello, from sunny' not in item.content"
      with_items: "{{app_index.results}}"

    - name: verify backend db response
      uri: url=http://{{item}}/db return_content=yes
      with_items: "{{groups.webserver}}"
      register: app_db

    - fail: msg="db failed to return content"
      when: "'Database Connected from' not in item.content"
      with_items: "{{app_db.results}}"
```


### same thing done with roles 

create roles folder and then within that folder run
`ansible-galaxy init <role_name>`  creates basic structure for each role
for each role copy the tasks into `tasks/main.yml`
eg for control file would look like
role structure:
```
roles/apache2
├── defaults
│   └── main.yml # default values which will be replace any {{ variables }}
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── README.md
├── tasks
│   └── main.yml
└── vars
    └── main.yml # another place where variables can be placed
```

```
- name: install tools
  apt: name={{item}} state=present update_cache=yes
  with_items:
    - curl
    - python-httplib2
```
then tasks in original file are replaced with role

control
```
---
- hosts: control
  become: true
  roles:
    - control
```
database example
```
---
- hosts: database
  become: true
  roles:
    - mysql # there is no need to specify anything for the handlers, only to set it in roles/name/handlaers/main.yml

```
when template is being used, it is saved as a file in roles/templates and path to it in configuration is just set as `src=<filename>`
files should be copied into files folder

used to reference other playbooks so then shouldn't need to be applied individually

```
---
- include: control.yml
- include: database.yml
- include: webserver.yml
- include: loadbalancer.yml
```

## Using facts / dynamic variables

Variables can be added in three ways within a file:
vars:
  foo: bar
  foo=bar
vars_files:
  - /path/to/vars/file.yml
  - /path/to/another/file.yml
vars_prompt:
  - name: web_domain # name of the variable
    prompt: Web domain # friendly name for which user will be prompted

ansible -m setup <host_name> # it executes just gathering facts step

<beginning>
---
- hosts: database
  become: true
  tasks:
    - name: install tools
      apt: name={{item}} state=present update_cache=yes
      with_items:
        - python-mysqldb

    - name: install mysql-server
      apt: name=mysql-server state=present update_cache=yes

    - name: ensure mysql listening on all ports
      lineinfile: dest=/etc/mysql/my.cnf regexp=^bind-address
                  line="bind-address = {{ ansible_eth1.ipv4.address }}"
                  # this will take address from gather facts command
      notify: restart mysql

    - name: make sure mysql started
      service: name=mysql state=started enabled=yes

    - name: create demo database
      mysql_db: name={{ db_name }} state=present

    - name: create demo user
      mysql_user: name={{ db_user_name }} password={{ db_user_pass }} priv={{ db_name }}.*:ALL
                  host='{{ db_user_host }}' state=present

  handlers:
    - name: restart mysql
      service: name=mysql state=restarted
<end>
# add variable values to roles/<role_name>/defaults/main.yml as this:
# these are the lowest priority variables
<beginning>
---
db_name: myapp
db_user_name: dbuser
db_user_pass: dbpass
db_user_host: localhost
<end>

ansible-playbook database.yml -e db_name=myapp... # variable passed via command line
# variables passed like this are the highest priority
# variables can also be stored within roles/<role_name>/vars/main.yml,
# downside of this is that it needs to be done for each role individually
# vars can also be put within a task
    - name: create demo database
      mysql_db: name={{ db_name }} state=present
      vars: 
        db_name=myapp
# vars can also be added in play(main) level
<beginning> "database"
---
- hosts: database
  become: true
  vars:
    db_name=myapp
  roles:
    - mysql
<end>
# or within roles
<beginning> "database"
---
- hosts: database
  become: true
  roles:
    - { role: mysql, db_name: demo,
                     db_user_name: demo,
                     db_user_pass: demo,
                     db_user_host: '%' }
<end>
## using global variables ##
# define global variables inside group_vars/all.yml
<beginning> "all.yml"
---
db_name: demo
db_user: demo
db_pass: demo
<end>
# in case variable names are different somewhere in the code point to those variables to these
<beginning> "database"
---
- hosts: database
  become: true
  roles:
    - role: mysql
      # db_name: demo - this isn't needed as this variable name is the same
      db_user_name: "{{ db_user }}"
      db_user_pass: "{{ db_pass }}"
      db_user_host: '%'
<end>
# in case they are the same, they don't need to be specifically stated anywhere else
<beginning> "webserver"
---
- hosts: webserver
  become: true
  roles:
    - apache2
    - demo_app
<end>

## encrypting variables ##
ansible-vault create <vault_filename> # do this within a folder where you want it
ansible-vault edit <vault_filename> # to change the content after it has been saved
# then point the unencrypted variable to the encyrpted one
<beginning>
---
db_name: demo
db_user: demo
db_pass: "{{ vault_db_pass }}" # name of the value from the vault file
<end>
# when running a playbok which contains a encrypted pass
ansible-playbook --ask-vault-pass
# or store this pass in a file outside of a folders which are pushed to a repo as plain text
# this can be done each time via command line
ansible-playbook --vault-password-file <path_to_file>
# or better put it into ansible.cfg as
vault_password_file = <path_to_file>

### using dictionary ###

# dictionary is inserted in roles/<role_name>/defaults/main.yml
<beginning>
---
sites: # item
  myapp: # key
    frontend: 80 # value
    backend: 80
<end>
# and then used as with_dict
<beginning>
    - name: configure nginx site
      template: src=templates/nginx.conf.j2 dest=/etc/nginx/sites-available/{{ item.key }} mode=0644
      # it is going to look for item.key which in this case is myapp from sites.myapp
      with_dict: "{{sites}}"
      notify: restart nginx
<end>

### using condition ###

# conditions can be added to some commands, example
- name: get active sites
  shell: ls -1 /etc/nginx/sites-enabled
  register: active # register result within variable "active"

- name: de-activate default nginx site
  file: path=/etc/nginx/sites-enabled/{{ item }} state=absent
  with_items: "{{active.stdout_lines}}"
  when: item not in sites
  notify: restart nginx


### speeding everything up ###
gather_facts: false # before tasks where it is possible

<beginning>
---
- hosts: loadbalancer
  become: true
  gather_facts: false
  tasks:...
<end>

update_cache # can be used once on site.yml, not in each role
<beginning> "site.yml"
---
- hosts: all
  become: true
  gather_facts: false
  tasks:
    - name: update apt cache
      apt: update_cache=yes cache_valid_time=86400

- include: control.yml
- include: database.yml
- include: webserver.yml
- include: loadbalancer.yml
<end>
ansible-playbook site.yml --limit app01 # limits a specific host but applies all rules from site.yml

changed_when: false # add on site check where it returns that something looks like it has changed but actually hasn't
# this can also be used with some expression changed_when: "something != something"
...
  tasks:
    - name: verify nginx service
      command: service nginx status
      changed_when: false
...
failed_when: # used in similar way as changed_when


  ## tagging ##

# each task or role can be tagged
ansible-playbook site.yml --tags "<tag_name>" # executes only tasks which are marked with that tag
ansible-playbook site.yml --skip-tags "<tag_name>" # same thing to skip ceertain tasks
# it helps to mark all steps which install packeges to be skipped, speeds things up

ansible-playbook site.yml --step # asks for each step should it be executed
ansible-playbook site.yml --list-tasks # shows all tasks
ansible-playbook site.yml --start-at-task "<task_name>"
ansible-playbook site.yml --limit @/path_to_file.retry # retries only failed hosts
ansible-playbook --syntax-check site.yml # just checks syntax
ansible-playbook --check site.yml # dry run, preview of things that will be done


  ## debugging ##

# used when a variable value needs to be checked or when just some message needs to be
# displayed during execution
- debug: var=active.stdout_lines # prints out a value for active.stdout_lines variable
- debug: var=vars # prints out values for all variables

## Working with AWS dynamic inventory

Computer from which this script is launced must have appropriate permissions set and credentials added to ~/.aws/credentials
From the Ansible website locate and download ec2.py and ec2.ini files
Save them anywhere on the computer and make ec2.py executable by chmod +x
If working with instances in private subnets, in ec2.ini file change 
  destination_variable to private_dns_name and 
  vpc_destination_variable to private_ip_address

to check if the script works from  run ./ec2.py --list, it shold return a list of all available hosts
Specify group_vars or any vars files with 
  remote_username and 
  ansible_private_key_file values
In order to use ansible with specific instances run 
  ansible -i <path_to>ec2.py <tag_Name...> -m command
  ansible -i ec2.py tag_Environment_Staging -m ping

In order to use it with ansible-playbook
 ansible-playbook -i ec2.py --limit tag_Environment_Staging playbook.yml

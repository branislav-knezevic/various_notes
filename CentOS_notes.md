# Centos notes

`find / -name [name] ` search recursevly in centos
`locate <filename> ` same as find, but faster
  run sudo updatedb first and each time before search
  some paths are excluded, like /tmp - list is in /etc/updatedb.conf
`iptables -L -n ` check open firewall ports
`hostname ` compute name
`pwgen ` password generator (needs to be intsalled)
`wget [url] ` download file
`curl ` transfer data between the server, also used for download
`mkdir ` create folder
`mv [old path] [new path] ` move file
`cp [old path] [new path] ` copy file
`rm [path] ` remove file
`netstat -plntu ` checks open ports
`nmap -sT -O localhost ` also to check open ports, nmap needs to be installed first
`tail -100 /var/log/messages ` show last 100 logged messages
`tail -f /var/log/graylog-server/server.log ` live log update when opened in new window/session
`less +F ` or shift+f within less command
`rpm --imprt [url] ` adding package repository
`echo '[some text...]' | tee [file path] ` creates specified file with specified text
`service [service name] start/stop/restart... ` way to work with services
`service [service name] configtest ` tests if service is configured in a proper way
`systemctl ` usefull for services
`systemctl start/stop/status/enable... [service name]` work with services
`chkconfig ` also used with services
`chkconfig [service name] on ` same as systemctl enable
`htpasswd ` used to store credentials
`wget -qO- http://ipecho.net/plain ; echo ` check public IP
`ggVG ` vim select all
`ps ax|grep log ` shows which file is using which config (grep is used for searching)
`ps aux | grep 'foo\|bar' ` searches for lines which contain either foo or bar
`date ` shows date and time on the server
`echo $? ` shows last logged error
`ls -lt ` lists files sorted by time modified
`df -h ` disk space
`du --max-depth 1 ` checking from root level what is taking up disk space
`lsblk ` view mounted disk drives
`kill -KILL 45379 ` kill specific process
`which [name of executable] ` shows the path of the executable
`htop ` chekc RAM and CPU usage
`yum whatprovides netstat ` get info about a command which you need but it isn't installed
`:setf conf ` set syntax for conf files in Vim if not visibile immediatly
`sudo nmtui ` activate network when CentOS is first installed
`sudo lid <username> ` shows groups for a specific username
`sudo lid -g <groupname> ` shows members of specified group
`export STA_GOD=NESTO ` sets velue NESTO variable to variable STA_GOD
`echo $STA_GOD ` returns the value of STA_GOD
`unset STA_GOD ` sets to default
`mc ` total commnader
`nmtui ` visual network interface
`sudo !! ` runs previously ran command with sudo privileges
navigating in terminal:
  `ctrl+a ` go to beginning
  `ctrl+e ` go to end
  `alt+b  ` one word back
  `ctrl+b ` one letter back
  `alt+f  ` one word forward
  `ctrl+f ` one letter forward
  `ctrl+k ` cuts text right of the coursor
  `ctrl+u ` same thing to the left
  `ctrl+y ` paste
  `ctrl+w ` erases one word to left (ctrl+backspace)
  `alt+. ` pastes argument from the previous command
`reset` resets the terminal
`journalctl --since "1 hour ago" ` userfull for logs
	journalctl --since "1 day ago" --until "1 hour ago"
	journalctl --since <YYYY-MM-DD HH:MM:SS>
	journalctl -u <service_name>
		journalctl -u nginx.service
	journalctl _UID=<user_id> # obtain user_id via id -u <username>
	journalctl -f # active logs
`sudo usermod -a -G rabbitmq branislav-knezevic ` add user to existing group
`watch "<some_command>" ` live show of command
`screen ` terminal multiplexer and good for remembering sessinos
	ls # shows sessions
	-x <session_id> # attaches the session
	ctrl+a +
			c # new screen
			n # toggle screens
			d # detach
			k # kill screen
			S # split horizontally
			V # split vertically
			tab # switch between split screens
			X # remove split
`tmux ` same likie screen but better :)
	list-sessions # shows list of available sessions
	new -s <session_name> # create new session with specific name
	attach -t <session_name> # attach to existing session
	ctrl+d # when within a session to exit current pane
	ctrl+b +
			c # new window
			, # rename current window
			p # previous window
			n # next window
			w # list windows
			% # split vertically
			<arrow_key> # switch panes
			'"' # (") split vertically
			: # gives an option to type in commands
			: split-window # split vertically
			d # detach from a session
	changing (creating) a ~/.tmux.conf file with following content changes the default command to be ctrl+a instad of ctrl+b
		unbind C-b
		set -g prefix C-a


w # shows logged on users with some basic login info
who # almost the same, just little less info
`&& `  "and"
  `prog1 && prog2 ` runs prog2 only if prog1 has completed successfully
`cut ` can be used to splice content of documents
  `cut -d: -f1 /etc/passwd ` split /etc/passwd document by deliiter ":" and use the first element (f1)
`sort ` great for working in pipes, sorts things withing text files
	cat file.txt | sort -bf # sorts all rows by first letter
User related
	/etc/passwd # list of all users
	/etc/shadow # also some user info
	/etc/group # list of groups with members
iptables
	-L # list all rules
	--line-numbers # show rule order
	-A # append a rule at the end
	-I # insert a rule at the beginning
	-s # source IP, single ip or range
	-p # specify protocol
	--dport # destination port
	-j ACCEPT/DROP # what to apply
	-D INPUT/FORWARD/OUTPUT <rule nubmer> # deletes specified rule
	to clear chains,
		create file clear-all-rules
			# Empty the entire filter table
			*filter
			:INPUT ACCEPT [0:0]
			:FORWARD ACCEPT [0:0]
			:OUTPUT ACCEPT [0:0]
			COMMIT
		run iptables-restore < clear-all-rules
Meld # investigate, sometihg to compare files
/boot/grub/grub.cfg # data about the installed kernels
uname -r # current kernels
sudo apt-get autoremove # remove old downloaded unused kernels
clusterssh # ssh to multiple hosts at once
sudo fdisk -l # list all partitions
	# edit /etc/fstab if you want to permanenty mount some drives
sudo umount <drive_path> # to unmount
	# sudo umount /mnt/windows
http://catb.org/~esr/faqs/smart-questions.html # to read
www.kernel.org/doc/man-pages/
tar # take archive
	z # zip (gzip)
	c # create
	v # verbose
	f # file name
		tar -zcvf <archive_name.tar.gz> <desired_directory>
	x # extract
		tar -zxf <desired_arhcive_file>
script <log_file_name.log> # records a session to a specific file
  exit or ctrl+d to finish
	script -s myscript.log --timing=time.log
	# to replay
	scriptreplay -s myscript.log -t time.log # replays all the steps
	script -c '<command>' <file_name> # records output of the commaind into a file
lynx # command line tester for web pages
find . -type f | wc -l # command for recursive file counting
less /etc/*release # info about OS
less /proc/cpuinfo # CPU info
        can be used with | grep proc
less /proc/meminfo # memory info
    can be used with | grep mem
free -h # available memory
uname -a # kernel info
pushd /<folder>; pushd /<folder> # sets these two folder for easier switch
popd # switches between those two folders
du | sort -n # add soriting to this command
systemd-cgls # tree view for services
diff -qr # differences between files
colordiff # even better :)
        sometimes it is used diff -gr | colordiff
lsof -i # shows open files, something like that
strace -p <process_id> -e trace=file,network #
vmstat -S M # usage info on VM
        iostat
        mpstat
tcpdump -ni eth0 dst port 80  # used to troubleshoot networking
find /var/log -mmin 1 # find files in the specific location which were modified within a last minute
ssh-copy-id -i <path_to_the_ssh.pub> <destination_server> # copy public key to a destination server
ssh-add # adds the ssh key somewhere so it can be forwarded to another server 
sudo yum list installed # list of all installed packages
env # show all enviroenment variables
openssl x509 -text -noout -in <certificate_name>.crt # details about the certificate
`!!` # to use output of the previous command in the next one
openssl x509 -enddate -noout -in /etc/ssl/certs/peer.pem # check end date of specific certificate    
curl https://ipinfo.io/ip # get public IP
openssl rand -base64 15 # generate random password
host <url> # check if it is resolvable
python -m SimpleHTTPServer 8000 # start a simple web server, goot for port testing
curl -s -w 'Testing Website Response Time for :%{url_effective}\n\nLookup Time:\t\t%{time_namelookup}\nConnect Time:\t\t%{time_connect}\nAppCon Time:\t\t%{time_appconnect}\nRedirect
Time:\t\t%{time_redirect}\nPre-transfer Time:\t%{time_pretransfer}\nStart-transfer Time:\t%{time_starttransfer}\n\nTotal Time:\t\t%{time_total}\n' -o /dev/null http://virgin01.devtech-labs.com:18080
# testing response time of a website
mtr -rn -P <port> <ip> # testing Response time of website
ss # simlar like netstat
ps -<nesto> UID -o cmd # check on virgin4 machine, checks which command is ran for spcific process ID
/var/log/dpkg.log # usefull things about installed packages
`zipgrep` searching for stuff within zip, jar... files
`cat <filename> | awk '{print $5}' | sort -rn | uniq` check for unique values in a log file based on 5th column
`echo $?` exit code of the last executed command


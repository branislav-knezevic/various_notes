# Linux notes

## Markdown formated

`rsync` used to copy files via ssh between multiple systems
`rsync -zarvh <user>@<ip>:<path_to_file_on_remote> <path_on_local>`
eg:  
`rsync -zarvh branislav-knezevic@192.168.87.34:/tmp/privkey3.pem /tmp`

`ssh-keygen` to generate a ssh keypair
`ssh-keygen -t rsa -b 4096 -C "bknezevic"`

`ln` creating links from file to file
`ln file1 file2` creates a normal links
`ln -s file1 file2` creates a symbolic link
eg:
`sudo ln -s ~/Projects/Private/scripts/ec2_info.sh  /usr/bin/ec2_info`

### General

`who` shows who is logged on to the computer
`tty` shows which terminal console is used
`w` some basic OS info (up time, logged on users...)
`logout/exit/ctrl+d` all the same thing
`echo $VARIABLE_NAME` shows the value of the variable
`chsh -s <path_to_shell>` sets that shell as default
`ufw allow <port_number>` lets certain port through firewall UBUNTU
`ip addr` check IP on CENTOS
`![command]` runs the last command assigned, !gre will run last grep command (if it was ran previously)
`!?[key word]` runs last command which contains this keyword (command, part of the path...)
`!$` represents the last argument, ll /etc/www will list files and cd!$ will enter the same folder
`history` shows all commands which have been ran
`ctrl+r` searches the command history, esc to edit, enter to run

### Viewing files

`cat [file path]` like a read only command for files
`tac [file path]` same as cat just from end to start
`cat /etc/shells` lists the available shells
`cat -vet [file path]` shows the file with hidden characters
`dos2unix [file path]` converts file to unix, removing any hidden characters
`tail -f [file path]` keeps the log file opened and updates it. good for usage if services are restarted in a new window
`cut -f[column1],[column2] -d"[separator]" [file path]` to show only certain columns
eg:
`cut -f1,3 -d":" /etc/file1.csv`

`sort -k[column1] -t"[separator]" [file path]` to sort by certain column
eg:
`sort -k4 -t":" /etc file1.csv`
`less` reading file from end to beginning
`/<word>` searches for that word forwards
`?<word>` searches backward

`head -n <number>` how many lines to show
`tail -n <number>` how many lines to show
`tail -f` live update, good for logs
`diff <file1> <file2>` comparing two files
`meld <file1> <file2>` better choice for file comparisment, needs to be installed
`stat <file name>` shows statistic about the file, access, modify...

### File/directory manipulation

`cp [file path] [file path]` copying file from current location to the new one. If second name is different but the path is same as the source, then it will create same file with different name
`mv [file path] [file path]` move file, if both path are same and name is different, it will then rename the file
`cp|mv|ll|ls -R` recursive copy/move/list of files
`mkdir` create directory
`mkdir -p` can create multiple directories within 
eg: 
`mkrid -p folder1/folder2` creates both folders (f2 within f1)
`rm` delete file
`rmdir` remove folder
`cd` without any arguments goes to home directory
`ls` list directory
File and folder permissions: 
```
drwxr-xr-x. 4 root root 44 May 13 05:25 folder1.1
	d # type of the file - directory in this case
	rwx # permissions for root user (as root is mentioned after number 4)
	r-x # permissions for root group
	r-x. # permission for everyone else
	4 # number of links which his pointing to the file. directory alway has min of 2
	root # user which has the permissions on this file
	root # group which has the permission on this file
	44 #
	May 13 05:25 # date/dime modified
	folder1.1 # file/folder name
```
`ll -lr` list files and sort by time modified
`ll -lrt` reverse listing
`dd` for imaging disk
`tar -cvf [file path/name.tar] [source folder]` to archive/zip files -c create, -v verbose, -f to which file
`tar -cvzf` same as above, just uses gZip which zips files more
`tar -tf [file path]` views the content of the tar archive. -z can be added if it is gZip
`du -sh [folder path]` check size of folder
`time [command]` measures the time it takes for command to execute
`touch [file path/file name]` creates empty file or used to changed modified time for existing file
`find [criteria] -exec [command]` executes specified command on all results of the find command
 eg: 
`find /usr/share -maxdepth 3 -name '*.pdf' -exec ls -lh {} \;` find all files in /usr/share which are three folders down and have a .pdf extension, show ls -lh properties for each of them
`find /usr/share -maxdepth 3 -size +138K` return all files three levels down from /usr/share which are bigger than 138K
`find . -name "<file_name>" -type f -delete` locate all files with specific name recursively from current dir and delete them
`find . -name "<dir_name>" -type d -exec rm -rf {} +` locate all directories with specific name recursively from current dir and delete them 

`ls [folder path] 1> [file path/file name]` ls is just a example command, this will store the output of this command in specified file. Number 1 is optional in this case
`ls [folder path] 1>> [file path/file name]` same as above, just appends to the file, doesn't create a new one
`ls [folder path] 2> [file path/file name]` this will record only errors
`ls [folder path] 1> [file path/file name] 2>&1` this will record both info and error in the same file
`set -o` shows some options for the shell, noclobber is point of interest at this moment
`set -o noclobber` this changes state from off to on for this command. This will turn on protection from overwritting the file. This works only during this session. Permamently it can be set by using login scripts
`df -h` "disk free" displays the free disk space
`du -h` "disk usage"
`which <app_name>` shows the path to home folder of this application
`tee` uses to output result both to command line and the file
eg:
`ll /etc | tee /temp/somefile` will show the content of /etc folder on the screen but also save it in the /temp/somefile file

`find <where> -name <what>` locate any file on disk
`  find <where> -name <what> -exec <cp, mv...> {} <where> \;` do something with results from find
`  -maxdepth <number>` how many directories to search in depth
`  -size +<number>k` size in kb
eg:
`find /boot -size +20000k`

`locate <filename>` same as find, but faster
`sudo updatedb` run first and each time before search
some paths are excluded, like /tmp - list is in /etc/updatedb.conf

`sed` searching, find and replace, insertion or deletion
eg.
`sed 's/<word1>/<word2>/g' <source_file> > <destination_file>` searches for `<word1>` in `<source_file>` replaces it with `<word2>` and outputs the result into `<destination_file>`


### Proceesses

uptime # shows uptime of the computer and load average data
	# 1/5/15 minutes - should be less than number of cores on the machine
jobs # checks running jobs
ps # something similar to jobs, list of running processes
  ps -l
  ps -f
  ps -ef # shows all processes
  ps -ef | grep [process name] # show all processes with certain name
pgrep [process name] # same as ps -ef | grep [process name]
kill [process number] # stop/kill process
pkill [process name] # stop/kill process
killall [process name] # stop/kill all process threads
kill -9 or kill -kill [process name] # stops process by force

--- searching regular expressions ---

grep [what] [where] # searching for the text
    grep Server /etc/config/root.conf # searches for word Server in /etc/config/root.conf file
  grep -i # not case sensitive search
  '\b[word]\b' # searches for specific word , without \b it will look for variations e.g. words, sword...
  # \b stands for boundary
  '^[word]\b' # searches for 'word' only at the beginning of a line
grep -ve '^#' -ve '^$' [file] # returns file without blank lines or comments
  -v # inverses the search
  -e # allows more than one expression
  ^# # searches for all comment lines
  ^$ # searches for blank lines
sed -i '/^#/d; /^$/d' [file] # deletes all blank and commented lines
  -i # switch that specifies that file will be edited, without it it will show what could happen
  # without -i it would be like using the grep command
grep -E # searching for more complex regular expressions
  grep -E '[A-Z]{1,2}[0-9]{1,2}[A-Z]?\s[0-9][A-Z]{2}' postcode
    [A-Z]{1,2} # search minimum 1 and maximum 2 upper case characters
	[0-9]{1,2} # search minimum 1 and maximum 2 numbers
	[A-Z]? # optional character
	\s # space
	[0-9] # single number
    [A-Z]{2} # two upper case characters

--- working with Vim ---

editing in Vim
  i # insert at coursor position
  I # insert at start of the current line
  a # append to coursor position
  A # append to end of current line
  o # new line below current position
  O # new line above current position
  G # end of the file
  [0-9]G # got to certain line defined by line number
  w # move forward one word
  [0-9]w # moves forward for number of words
  b # move backward one word
  [0-9]b # moves backward for number of words
  x # deletes one character to the right (like del key)
  [0-9]x # deletes that many characters
  dw # deletes word right of the cursor
  [0-9]dw # deletes certain number of words
  $ # end of the line
  ^ # beginning of the line
  set number # enables line numbers
  set nonumber # disables line numbers
  syntax on # enable syntax
  u # undo changes
vi +[number of line] [file_name] # opens vi and goes to specific line number
vi +/[string] [file_name] # goes to first appearance of given string
last line mode
  :r [path/file] # open existing file within vi
  :[number],[number]w [file/folder] # copies lines from [number] to [number] to new file named [file/folder]
  :%w [file/folder] # copies whole content to new file
  :r![command] # adds the output of the command to file
  :x # save and exit
search and replace
  :%s/[word]/[word]/ # search the whole document and replace
    :%s/John/Peter/ # replace word John with word Peter in the whole document
    :1,20s/John/Peter/ # does the replacement between specified lines
	:10,30s/^/    / # creates indent on specified lines
  /[word] # searches for specific word
  n # goes to next word
Customizing .vimrc
set showmode nonumber nohlsearch
set ai ts=4 expandtab
abbr _sh #!/bin/bash
nmap <C-N> :set invnumber<CR>





--------------------------
-- eli the computer guy --
--------------------------

adduser [name] # add user on linux
	sudo adduser Bane # adds user Bane
userdel [name] # deletes user account
/etc/passwd # main file which contains info about existing users
passwd [name] # change password for a user
groupadd [name] # create group
groupdel [name] # deletes group
adduser [user_name] [group_name] # add user to group
deluser  [user_name] [group_name] # remove user from group
/etc/group # main file about groups
Permissions:
-rw-r--r--. 1 root root # permissions example
7:7:7 # owner : group : everyone
  4 # read
  2 # write
  1 # execute
chmod 777 [file_name] # change permission on file/folder
chown [user_name] [file_name] # change owner of file/folder
chgrp [user_name] [file_name] # change group of file/folder

 -- network --

ifconfig # same as ipconfig
sudo /etc/init.d/networking restart # to restart network service, probably can be don oin a different way
dhclient # ip release/renew

 -- backup --

tar -cvpzf [path/name].tar.gz --exclude=[folder path/name] [folder which is being backed up]
  c # create backup file
  v # verbose
  p # preserve permissions
  z # compress backup
  f # set filename for backup
	sudo tar -cvpzf /backupFolder/backup.tar.gz --exclude=/etc/somefolder /etc
	# backs up /etc folder without /etc/somefolder to file /backupFolder/backup.tar.gz
tar -xvpzf /backupFolder/backup.tar.gz -C [/path/name of folder]
  x # extract information from tar file
  v # verbose
  p # preserve permissions
  z # uncompress
  f # specify filename
    sudo tar /backupFolder/backup.tar.gz -C /recoveryFolder
	# extract all files from /backupFolder/backup.tar.gz to /recoveryFolder
crontab -e # schedule a job
/etc/crontab # system wide crontab, has additional field to specify a user
  e # edit crontab job file
 m    h    dom    m    dow
0-59 0-23  1-31  1-12  0-6
  m   # minutes
  h   # hour
  dom # day of month
  m   # month
  dow # day of week, 0 is Sunday
    30 2 * * 2 [command/file] # schedule job to run at 2.30 every Tuesday


-------------------------------------------------------------------------------
System layout
/
|---bin # basic operating system commands are stored here (move, copy, list...)
|---boot # kernel and kernel files
|---dev # all devices, HDD, CPU... all disks are named as sd<something>
|---etc # system configuration and configuration for installed apps
|---home # home directory for all users which are not users
|---lib # like dll files in Win, libraris which programs used
|---lib64 # same as above
|---media # somewhere mnt - mount directory where automounted things go
|---opt # optional software, ususally on desktops, not servers
|---proc # directory for each process which is running
|---root # home of root user
|---run #
|---sbin # critical files which machine needs to get itself up and running - DO NOT TOUCH
|---sys #
|---tmp # temporary files, deleted on reboot
|---usr # none super essentias of binaries and commands, addition to bin
	|---lib # shared libraries
	|---sbin # admin commands
	|---share # things that might be common to multiple systems
|---var # various. variable
	|---log # has all system logs in it
```


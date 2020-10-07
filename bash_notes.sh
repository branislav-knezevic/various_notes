Bash scripting
	sublimeText # recommended editor
	&& # and - first command must be successful in order for the second one to execute
	|| # or - both will execute
	$<variable_name> # variable
	${<variable_name>} # can also be used like this
		<variable_name>="<variable_value>" # setting the variable
	`<command>` # using backtick (`) to use command within a variable
	# if script is executed with a bash/sh <script> it executes in new shell
	# if script is executed as . (or source) <script> it executes in the existing shell and variables from the script become then available in the shell
	# tested this with source, doesn't work as intended
	arguments
    $# # number of arguments that script was ran with
    $@ # all arguments
	  $0 # is always reservered as a variable for the name of the file
	  $1...$n # all other arguments in order
			content
			  echo argument 1 is ${1} argument 2 is ${2} argument 3 is ${3}
			run
				file.sh one two three
			output
	    	argument 1 is one argument 2 is two argument 3 is three
		# adding argument which doesn't exist may cause problems

  ## if loop ##

    if [[ condition ]]; then # before only single brackets were used
      #statements
    elif [[ condition ]]; then
      #statements
    else
      #statements
    fi
    if ((string_condition)) ; then # for strings (()) must be used
      #statements
    fi

	## for loop ##
		for arg in "$@"; do # $@ means all provided arguments
		  #statements
		done

		# or a different way
		for (( i = 0; i < 10; i++ )); do
		  #statements
		done

  ## comparison operateors ##
    eq | =  # equal
    ne | != # non equal
    lt | <  # less then
    gt | >  # greater than
    le | <= # less or equal
    ge | >= # greater or equal
			 | =~ # compares regex values
  ## value testers ##
    -n  # true if length of a string is non-zero
    -z  # true if length of a string is zero
		-f  # check if file exists

  ## functions ##
	function name(parameter) {
	  #statements
	}

set -e # setting this at the beggining will make the script to exit on error

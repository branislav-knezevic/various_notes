#!/bin/bash

# basic if testing
NAME=$1
GREETING="Hi There"
HAT_TIP="tip of the hat"
HEAD_SHAKE="shake head"

if [[ "$NAME" = "Dave" ]]; then
  echo $GREETING
elif [[ "$NAME" = "Steve" ]]; then
  echo $HAT_TIP
else
  echo $HEAD_SHAKE
fi


# using if to check number of arguments
NUM_REQUIRED_ARGS=2 # require exactly two arguments
num_args=$# # how many arguments were actually set
if [[ $num_args -lt NUM_REQUIRED_ARGS ]]; then
  echo "Not enough arguments call this script with
  ./${0} <name> <number>"
  exit 1 # exit with generic code 1 (error)
fi

# -z and -n
notnully="this is not null"
nully=""

if [[ -n "$notnully" ]]; then
  echo "this is not at all nully"
fi

if [[ -z "$nully" ]]; then
  echo "nully/zero (length)"
fi


# comaprison opeartor, single vs double parenthasis
num1=$1
num2=$2
if (($num1 == $num2)); then
  echo "${num1} is equal to ${num2}"
fi

for (( i = 0; i < 10; i++ )); do
  #statements
done

function name(parameter) {
  #statements
}

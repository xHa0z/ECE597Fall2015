#! /bin/bash 

#if [$# -lt 4 ]; then
#	echo "Usage: $ <device1 id> ,<device2 id>, <LOW TEMP>, <HIGH TEMP>"
#    	exit 0
#fi

sensor1=$1
sensor2=$2

# get sensor temp
declare -i TMP1=$(i2cget -y 1 $1 0)
declare -i TMP2=$(i2cget -y 1 $2 0)

echo "The senor 1 is "$1" and its temp is $TMP1 degree C"
echo "The senor 2 is "$2" and its temp is $TMP2 degree C"

# set senor alert
tempLOW=$3
tempHIGH=$4

echo "The low senor 1 is set to $3 degree."
echo "The high senor 2 is set to $4 degree."

#set senor 1 config byte
i2cset -y 1 $1 1 0x04
i2cset -y 1 $2 1 0x04
#set low temp
i2cset -y 1 $1 2 $3
i2cset -y 1 $2 2 $3
#set high temp
i2cset -y 1 $1 3 $4
i2cset -y 1 $1 3 $4






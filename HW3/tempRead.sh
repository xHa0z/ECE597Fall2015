#! /bin/bash
declare -i TMP1=$(i2cget -y 1 0x48 0)
declare -i TMP2=$(i2cget -y 1 0x4a 0)

TMP1F=$((TMP1 * 9/5 + 32))
TMP2F=$((TMP2 * 9/5 + 32))

echo "The senor 1 is $TMP1F degree F."
echo "The senor 2 is $TMP2F degree F."


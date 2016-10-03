#!/bin/bash

# simulate long running build with "colored" output

for i in `seq 1 50`;
do
    echo $i
    echo -e "Hello\033[31m colors\e[0m!"
    ls -la
    sleep 1
done  

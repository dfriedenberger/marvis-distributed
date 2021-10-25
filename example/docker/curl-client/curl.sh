#!/bin/sh

while true;
do
    ping -c 1 server

    curl --max-time 1.0 http://server/hello
    echo ""
    
    sleep 3
done

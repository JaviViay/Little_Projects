#!/bin/bash

subnet="192.168.1" #common domestic ip range

echo "Starting scan..."
for terminal in {1..255}; do
	ip="${subnet}.${terminal}"
	if ping -c 1 -W 1 "$ip" >/dev/null 2>&1; then #with -W adjust number of seconds
		echo "Found terminal: $ip"
	fi
done
echo "Scan done"
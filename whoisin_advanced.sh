#!/bin/bash

subnet="192.168.1" #common domestic ip range

echo -e "\e[34mScanning with Nmap...\e[0m"
nmap -T4 -sn "${subnet}.0/24" -oG - | awk '/Up/{print "Found terminal:", $2}' | sed 's/Nmap://'

echo -e "\e[33mScanning with arp-scan...\e[0m"
sudo arp-scan --localnet | grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' | awk '{print "Found terminal:", $1}'

echo "Scan done"
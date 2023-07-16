#!/bin/bash
read -p $'\e[34m[*] Enter the target IP or IP range: \e[0m' target
echo "1. Basic Nmap"
echo "2. Advanced Nmap"
echo "3. Custom Nmap"
read -p $'\e[34m[*] Select an option: \e[0m' type_nmap

if [ "$type_nmap" == "1" ]; then
    nmap "$target"
fi
if [ "$type_nmap" == "2" ]; then
    nmap -p- -sV -sC --open -n -Pn --min-rate 5000 "$target"
fi
if [ "$type_nmap" == "3" ]; then
    read -p $'\e[31m[*] Show all ports or only open? (all/open): \e[0m' only_open
    read -p $'\e[31m[*] Enable script scanning? (y/n): \e[0m' enable_scripts
    read -p $'\e[31m[*] Enable version detection? (y/n): \e[0m' enable_version
    read -p $'\e[31m[*] Do it quick? (y/n): \e[0m' quick

    nmap_command="nmap"

    if [ "$only_open" == "open" ]; then
        nmap_command+=" --open"
    fi
    if [ "$enable_scripts" == "y" ]; then
        nmap_command+=" -sC"
    fi
    if [ "$enable_version" == "y" ]; then
        nmap_command+=" -sV"
    fi
    if [ "$quick" == "y" ]; then
        nmap_command+=" --min-rate 5000 -Pn -n"
    fi

    nmap_command+=" $target"
    eval "$nmap_command"
fi
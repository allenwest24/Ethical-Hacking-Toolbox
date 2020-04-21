# Network-Scanner
My version of netdiscover
- Shows what kinds of devices are in our network

# Motivations for making this (Future builds that require this)
- Address resolution
    - Pair the IP address and the local IP address of a network
- Once we are in the same network as other people we are potentially vulnerable
- ARP spoofing 
- MITM
- See info coming through the network 

# Scapy
- Send and recieve packets

# ARP
- Stands for address resolution protocol

# How it works
- Make an ARP request
- Broadcast the request
- Get a response
- Handle that response
- Python3 compatible

# Usage
- python network_scanner.py -i (IP address here)

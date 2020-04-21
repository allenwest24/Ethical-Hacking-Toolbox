# ARP-Spoofer
Used in MITM exploits.

## Purpose & Background
Built a network scanner previously to show us mac addresses and paired IP addressed. We can use that to 
manipulate the data. Since we don't need a request to send a response, we can send a response. The router 
will think we are the target and the target will think we are the router.

## IP Forwarding
There are going to be packets going through our machine because it is in the middle. Our machine has to 
forward the packets to the target and its router. 
    - root@kali:~# echo 1 > /proc/sys/net/ipv4/ip forward

## Strategy
- Used the network scanner I previously built to find the MAC address of the target.
- To check the ARP table to see if it worked:
    - root@kali:~# arp -a

## Usage
python3 arpPosion.py -t ##.#.#.# -g ##.#.#.#

# Main file for my Network scanner

# Lets us deal with ARP
import scapy.all as scapy

import optparse

#----------------------------------------------------------------------------------------------------------------------------------------------

def get_user_input():
    # Format for giving the desired IP address
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")

    (user_input,arguments) = parse_object.parse_args()

    # If none were entered ask for one
    if not user_input.ip_address:
        print("Enter IP Address")

    return user_input

#----------------------------------------------------------------------------------------------------------------------------------------------


def scan_my_network(ip):
    # Create ARP Request
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    
    # Broadcast it
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    
    # Package and send
    combined_packet = broadcast_packet/arp_request_packet
    
    # Handle the result
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

#----------------------------------------------------------------------------------------------------------------------------------------------

# Call everything
user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)

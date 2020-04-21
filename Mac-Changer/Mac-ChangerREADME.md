# MAC CHANGER

Provides us an opportunity to change our MAC address. This will be explained below and in comments in the actual code.

You can use Pycharm as an IDE but I pretty much exclusively use vim.

# Mac and IP address refresher:
- Typing ifconfig gets us the mac address and IP addresses of the interfaces available.
- Networks work as such:
  - Devices connect to a router that connects to the internet which deals with requests and responses
  - If we ping google.com its a reuquest and we get the response from the router.
  - A public IP is what we use to connect to the internet. You don't want anyone to know your public IP address. 
  - Every device connected to the router has the same public IP.
  - They also have their own local id, specifying which device they are.
 
# Why do we want to change a mac address?
- Every interface like a wireless card or a wire connection has a mac address. Essentially a hadware number.
- It doesn't change if it changes devices.
- Change public IP by using a VPN.
- Routers can say "You can connect if you have this mac address"
- So if we want to connect to a network, we can change our mac address to be one that it will accept.

# Manual change
- We can do this manually through the following commands:
  - ifconfig <interface> down
  - macchanger -m <mac> <interface>
  - ifconfig <interface> up
  
- But that's not fun enough so I'm making my own mac changer.

# Current way to run this program:
- In terminal type:
  - python my_mac_changer.py --interface (interface) --mac (desired mac address)
  - you can search for <> arguments by running ifconfig in the command line
  - The program runs ifconfig and compares the desired address to the final result and returns "Success!" or "Error!" accordingly

# Main file for my mac changer

# So we can run command line processes in our python code
import subprocess
# To take inpout from the user
import optparse
# Used so we can work with regular expressions
import re

#---------------------------------------------------------------------------------------------------------------------------------------------------

def get_user_inputs():
    # Using the import optparse we set different optional arguments
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface", help="Interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="Ne Mac Address")

    # Create the tuple
    return parse_object.parse_args()

# Old Tests
# user_interface = user_inputs.interface
# user_mac_address = user_inputs.mac_address

# In order to hard code to test parts of code I will comment this out.
## Global variable to put the name of our interface. Ex: wlan0
#user_interface = ""
## Global variable to put the name of the interface we would like to change to our desired interface
#user_mac_address = ""

# Old Test
# print("MyMacChanger has been started.")

def change_mac_address(user_interface, user_mac_address):
    # Executing in command line using sub processes
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])

# Automating the check success process
def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    # Search for mac addresses in the output of the command ifconfig
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    
    # Here is where we take only the first mac address provided by ifconfig
    if new_mac:
        return new_mac.group(0)
    else:
        return None



# Replaced down here to tie all the code together
(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.user_mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

# Check to see if it changed to the proper mac address
if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")

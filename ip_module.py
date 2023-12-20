import ipaddress # Library used to check IP address validity
from clear_module import clear_screen
class IP: # Initialize object
    def __init__(self, ip_address=""):
        self.ip_address = ip_address

    def update(self): # Method to assign values to attributes of the IP class
        clear_screen()
        raw_ip = input("Enter IP Address: ")
        self.ip_address = raw_ip

    def display(self): # Method to display values of the attributes of the IP class
        clear_screen()
        info = f"IP Address: {self.ip_address}\n"
        print(info)

# Everything past this point is URL generation -->

    def generate_whatismyipaddress(self):
        try:
            # Check if the IP address is valid
            ip_obj = ipaddress.ip_address(self.ip_address)
            return f"https://whatismyipaddress.com/ip/{self.ip_address}"
        except ValueError:
            # If the IP address is invalid, return an error message
            return "No valid IP address provided."

    def generate_mxtoolbox(self):
        try:
            ip_obj = ipaddress.ip_address(self.ip_address)
            return f"https://mxtoolbox.com/SuperTool.aspx?action=ptr%3a{self.ip_address}&run=toolpage"
        except ValueError:
            return "No valid IP address provided."

    def generate_thatsthem(self):
        try:
            ip_obj = ipaddress.ip_address(self.ip_address)
            return f"https://thatsthem.com/ip/{self.ip_address}"
        except ValueError:
            return "No valid IP address provided."

    def generate_keycdn(self):
        try:
            ip_obj = ipaddress.ip_address(self.ip_address)
            return f"https://tools.keycdn.com/geo?host={self.ip_address}"
        except ValueError:
            return "No valid IP address provided."

    def generate_geolocation(self):
        try:
            ip_obj = ipaddress.ip_address(self.ip_address)
            return f"https://www.geolocation.com/?ip={self.ip_address}#ipresult"
        except ValueError:
            return "No valid IP address provided."

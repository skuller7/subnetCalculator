import random
import sys

def subnet_calc(ip_addres):
    try:
        print("\n")
        # Convert an address into octets ->|
        ip_octets = ip_address.split('.')

        if len(ip_octets) != 4:
            return False
        
        # Convert octets into integers (casting)
        octets = [int(octet) for octet in ip_octets]

        # Ensure all octets are within 0-255
        if not all(0 <= octet <= 255 for octet in octets):
            return False
        
        first = octets[0]
        second =  octets[1]

        if  (first == 10) or \
            (first == 172 and 16 <= second <= 31) or \
            (first == 192 and second == 168):
                return False
        
        if first == 127:
            return "Loopback address"
        
        if first == 169 and second == 254:
            return "APIPA (DHCP Auto-Assign)"
        
        if 224 <= first <= 239:
            return "Multicast Address IP"
        
        if 240 < first <= 255:
            return "Experimental Address/Reserved"
        

        if 1 <= first <= 223:
            return "Public IP"

        return False # Anything else is invalid

    except ValueError:
        return False

while True:
    ip_address =  input("## Please Enter your Desired ip address ###:")
    result = subnet_calc(ip_address)

    if result:
        print("The IP address is VALID: ", result)
        break
    else:
        print("The IP address is INVALID:", result)
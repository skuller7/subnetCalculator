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
        second = octets[1]
        third = octets[2]
        fourth = octets[3]

        if (first == 10):
            return "Private Address"

        if (first == 172 and 16 <= second <= 31):
            return "Private Address"

        if (first == 192 and second == 168):
            return "Private Address"
        
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

def subnetMask(mask):
    try:
        print("Subnet mask validation check")
        mask_octets = mask.split('.')

        if len(mask_octets != 4):
            return False
        
        octets = [int(octet) for octet in mask_octets]

        valid_values = [0, 128, 192, 224, 240, 248, 252, 254, 255]

        if not all(octet in valid_values for octet in octets):
            return False
        
        # Continuqous subnet mask ex : 255.0.255.0 not allowed

        binary_octets = []
        for octet in octets:
            binary_representation = bin(octet)[]
            return True


        first = octets[0]
        second = octets[1]
        third = octets[2]
        fourth = octets[3]

        if (first == 255):
            return "Class A Subnet"
        if (first == 255 and second == 255):
            return "Class B Subnet"
        if (first == 255 and second == 255 and third == 255):
            return "Class C Subnet"

    except ValueError:
        return False


while True:
    ip_address =  input("## Please Enter your Desired IP address ###:")
    mask_address = input("## Plesae Enter your Desired Subnet Mask ##")
    resultI = subnet_calc(ip_address)
    resultM = subnetMask(mask)

    if resultI:
        print("The IP address is VALID: ", resultI)
        break
    else:
        print("The IP address is INVALID:", resultI)

    if resultM:
        print("The Subnet Mask is VALID:", resultM)
        break
    else:
        print("Subnet Mask is INVALID:", resultM)
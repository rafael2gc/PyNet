ip_addr = input("Enter an IP Address: ")
print("{:^20}{:^20}{:^20}{:^20}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print('-' * 80)
octet = ip_addr.split('.')
print('{:^20}{:^20}{:^20}{:^20}'.format(
    octet[0], 
    octet[1], 
    octet[2], 
    octet[3] 
    )
)
print('{:^20}{:^20}{:^20}{:^20}'.format(bin(int(octet[0])), bin(int(octet[1])), bin(int(octet[2])), bin(int(octet[3]))))
print('{:^20}{:^20}{:^20}{:^20}'.format(hex(int(octet[0])), hex(int(octet[1])), hex(int(octet[2])), hex(int(octet[3]))))
print('-' * 80)
print()

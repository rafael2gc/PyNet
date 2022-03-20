from __future__ import print_function

try:
    ip_addr = raw_input("Entrerr - RAW ip add: ")
except NameError:
   ip_addr = input("Entrerr - INPUT ip add: ")
    
print(ip_addr)

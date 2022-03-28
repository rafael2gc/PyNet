from __future__ import print_function, unicode_literals
with open("show_ip_int_brief.txt") as f:
    contents = f.readlines()
int_fa4 = contents[5].strip()
fields = int_fa4.split()
intf = fields[0]
add = fields[1]
my_results = (intf, add)
print(my_results)

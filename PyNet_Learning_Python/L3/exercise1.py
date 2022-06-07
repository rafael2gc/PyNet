from __future__ import unicode_literals, print_function
from pprint import pprint

vlan_list = []
with open("show_vlan.txt") as f:
    show_vlan = f.read()

for line in show_vlan.splitlines():
    # Skip certain lines
    if "VLAN" in line or "-----" in line or line.startswith("  "):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id, vlan_name))

print()
pprint(vlan_list)
print()

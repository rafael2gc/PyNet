from pprint import pprint
f = open("show_arp.txt")
content = f.readlines()
f.close()
content = content[1:]
pprint(content)
new_list = content[0:3]
print()
pprint(new_list)
xx = "\n".join(new_list)
print(xx)
w = open("arp_entries.txt", mode="w")
w.write(xx)
w.close()

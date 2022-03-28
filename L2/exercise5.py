with open("show_ip_bgp_summ.txt") as f:
    contents = f.readlines()
local_as = contents[0]
peer_ip = contents[3]
#print(local_as, "\n", peer_ip)
alocal_as = local_as.split()
apeer_ip = peer_ip.split()
print(alocal_as[-1])
print(apeer_ip[0])

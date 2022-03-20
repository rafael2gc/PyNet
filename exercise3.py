#!/usr/bin/env python
from __future__ import print_function, unicode_literals
ipv6_add1 = '2620:0000:1cff:dead:bef1:0100:0005:003f'
IPV6_ADD2 = '2620:0000:1cff:dead:bef1:0100:0005:0059'
ipv6_add3 = '2620:0000:1cff:dead:bef1:0100:0005:000b'

print("")
print(" Is variavel1 equal to variavel2: {}".format(ipv6_add1 == IPV6_ADD2))
print(" Is variavel1 not equal to variavel2: {}".format(ipv6_add1 != ipv6_add3))
print("")
#ipv6_add1 == IPV6_ADD2
#ipv6_add1 != ipv6_add3
#print (ipv6_add1, IPV6_ADD2, ipv6_add3)

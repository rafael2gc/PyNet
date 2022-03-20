from __future__ import print_function, unicode_literals
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()
words = show_version.split()
print(words)
sn = words[2]
model = words[1]
print("Is Cisco contained in the model string? {}".format("CISCO" in words[1]))
print("Is Model contained in the model string? {}".format("881" in words[1]))
print(f"Serial Number is:{sn}")
print(f"Model is:{model}")

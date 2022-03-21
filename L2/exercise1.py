banner = "-" * 80
f = open("show_version.txt")
content = f.read()
print(content)
print(banner)
print(type(content))
f.close()
print(banner)
with open("show_version.txt") as z:
    output = z.readlines()
print(output)
print(banner)
print(type(output))
print(banner)

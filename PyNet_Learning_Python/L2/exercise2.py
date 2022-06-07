banner = "-" *60
my_list = ["10.1.1.99", "8.8.8.8", "214.136.55.44", "192.168.0.77", "13.18.33.12"]
#print(my_list)
my_list.append("7.7.7.7")
#print(banner)
#print(my_list)
#print(banner)
my_list.extend(["130.28.9.4", "22.11.0.12"])
#print(my_list)
#print(banner)
my_list = my_list + ["11.18.19.21", "45.67.87.90"]
print(my_list)
print(banner)
print("First IP in the List is: {}".format(my_list[0]))
print("Last IP in the List is: {}".format(my_list[-1]))
print(banner)
my_list.pop()
my_list.pop(0)
print(my_list)
print(banner)
my_list[0] = "2.2.2.2"
print(banner)
print(my_list)
print(banner)
print(my_list[0])


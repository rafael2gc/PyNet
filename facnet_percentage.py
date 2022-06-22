with open("base.txt") as f:
    contents = f.readlines()
#xx = contents.split("\n")
#for value in contents:
 #   print(value)
print(len(contents))
total = len(contents)
num_sw = input("Entre numero de switches upgraded: ")
num_sw = int(num_sw)
x = num_sw / total
print(f"Percentual concluido: {x*100}%")

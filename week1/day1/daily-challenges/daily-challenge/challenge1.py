number = input("Enter a number: ")
length = input("Enter a length: ")
nu_list = []
for i in range(int(length)):
    nu_list.append(int(number))
    number = int(number)*2
print(nu_list)
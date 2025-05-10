
def buildFamilyDict():
    family = {}
    while 1:
        name = input("Enter your name : ")
        if not name.isalpha():
            print("Invalid name. Please enter a valid name.")
            continue
        age = input("Enter your age : ")
        while not age.isdigit() or len(age) > 2:
            age = input("Invalid age. Please enter a valid age : ")
        age = int(age)
        family[name] = age
        cont = input("Do you want to add another family member? (y/n) : ")
        if cont.lower() != 'y':
            break
    return family

def familyCost():
    dict = buildFamilyDict()
    print("-"*20)
    totalCost = 0
    for name, age in dict.items():
        if age < 3:
            print(f"{name} is free")
        elif age <= 12:
            totalCost += 10
            print(f"{name} is 10$")
        else:
            totalCost += 15
            print(f"{name} is 15$")
    print(f"Total cost of the family is {totalCost}$")

familyCost()
def get_full_name(fName, lName, mName=""):
    return fName + " " + mName + " " + lName if mName else fName + " " + lName


print(get_full_name("John", "Doe"))
print(get_full_name("John", "Doe", "Smith"))
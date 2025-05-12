class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        if  len(kwargs) < 2:
            print("wrong number of arguments passed")
            return
        if not "name" in kwargs or not "gender" in kwargs:
            print("You must pass name and gender")
            return
        dict = {
            "name" : kwargs["name"],
            "age" : kwargs["age"] if "age" in kwargs else 0,
            "gender" : kwargs["gender"],
            "is_child" : True 
        }
        self.members.append(dict)
        print(f"Congrats {kwargs["name"]} have been added to the fam !")

    def is_18(self, name):
        for member in self.members:
            if name in member:
                return member["age"] > 18
        print("Not in the fam")

    def family_presentation(self):
        print(f"The fam Last name is : {self.last_name}")
        if not self.members:
            print("Empty :'(")
            return
        for mem in self.members:
            print(f"{mem["name"]} is a {mem["gender"]} aged {mem["age"]} years old, and", "is a child"if mem["is_child"] else "is not a child")


if __name__ == "__main__":
    mems =  [
            {'name':'Michael','age':10,'gender':'Male','is_child':True},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
    gg = Family("FreeMan", mems)   

    gg.born(name="abbass", gender="male")
    gg.family_presentation()
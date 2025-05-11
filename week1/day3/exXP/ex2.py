class Dog:
    def __init__(self, name, height):
        self.dName = name
        self.dHeight = height

    def bark(self):
        print(self.dName, " Woof Woof")

    def jump(self):
        print(self.dName, " jumped", self.dHeight*2, "cm high")

davids_dog = Dog("Rex", 50)
print(davids_dog.dName, "is", davids_dog.dHeight, "cm tall")
davids_dog.bark()
davids_dog.jump()
print("-"*20)
marys_dog = Dog("Fluffy", 20)
print(marys_dog.dName, "is", marys_dog.dHeight, "cm tall")
marys_dog.bark()
marys_dog.jump()
print("-"*20)
if davids_dog.dHeight > marys_dog.dHeight:
    print(davids_dog.dName, "is taller than", marys_dog.dName)

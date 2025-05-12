class Dog:
    def __init__(self,name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        return f"{self.name} is barking"
    def run_speed(self):
        return (self.weight/self.age*10)
    def fight(self, other_dog):
        if not isinstance(other_dog, Dog):
            print("Invalid Dog Object")
            return
        if other_dog == self:
            print("Cannot fight himself")
            return
        print(f"The Dog : {self.name} is fighting {other_dog.name}")
        myDog = self.run_speed() * self.weight
        heDog = other_dog.run_speed() * other_dog.weight
        if myDog == heDog:
            print("They have same power")
            return
        print("Dog", f"{self.name}" if myDog > heDog else f"{other_dog.name}", "won" )


if __name__ == "__main__":
    d1 = Dog("hamid", 1, 10)
    d2 = Dog("abass", 1, 10)
    d1.fight(d1)

class Zoo:
    def __init__(self, name):
        self.zoo_name = name
        self.animals = []
        self.animal_dict = {}

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            print(f"{animal} has been added to the zoo.")
        else:
            print(f"{animal} is already in the zoo.")

    def get_animals(self):
        if not self.animals:
            print("No animal in the zoo.")
        else:
            print(f"Animals in the {self.zoo_name} : {", ".join(self.animals)}")

    def sell_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} has been sold.")
        else:
            print(f"{animal} is not in the zoo.")

    def sort_animals(self):
        if not self.animals:
            print("No animal in the zoo.")
            return
        sorted_animals = sorted(self.animals)
        
        for animal in sorted_animals:
            if animal[0] not in self.animal_dict:
                self.animal_dict[animal[0]] = animal
            else:                
                self.animal_dict[animal[0]] = [self.animal_dict[animal[0]], animal]
        print("dict animals : ", self.animal_dict)

    def get_groups(self):
        if not self.animal_dict:
            print("No animal in the zoo")
            return
        for letter, animals in self.animal_dict.items():
            if isinstance(animals, list):
                print(f"{letter} : {', '.join(animals)}")
            else:
                print(f"{letter} : {animals}")
            print("-" * 20)

zoo = Zoo("My Zoo")
zoo.add_animal("Lion")
zoo.add_animal("Tiger")
zoo.add_animal("Elephant")
zoo.add_animal("Giraffe")
zoo.add_animal("Girfe")
zoo.add_animal("Zebra")
zoo.add_animal("Lion")  # Trying to add a duplicate animal
zoo.get_animals()
zoo.sell_animal("Tiger")
zoo.get_animals()
zoo.sort_animals()

zoo.get_groups()
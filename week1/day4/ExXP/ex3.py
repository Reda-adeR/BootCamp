from ex2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True
    
    def play(self, *args):
        print(", ".join(args), "all play together")

    def do_a_trick(self):
        if not self.trained:
            print(f"{self.name} is not trained")
            return
        import random
        tricks = [
            "does a barrel roll",
            "stands on his back legs",
            "shakes your hand",
            "plays dead"
        ]
        print(f"{self.name}", tricks[random.randint(0,3)])

pdog  = PetDog("hamid", 1, 10, False)

pdog.train()
pdog.play("adob", "batal", "matal", "khatar")
pdog.do_a_trick()
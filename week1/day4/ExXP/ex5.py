from ex4 import Family

class TheIncredibles(Family):
    def use_power(self, name):
        for mem in self.members:
            if mem['name'] == name:
                if mem['age'] >= 18:
                    print(f"{mem['name']}'s power is: {mem['power']}")
                else:
                    raise Exception(f"{mem['name']} is not 18 yo and cannot use power.")


    def incredible_presentation(self):
        print("Here is our powerful family:")
        super().family_presentation()


if __name__ == '__main__':
        
    incredible_members = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
    ]

    incredibles = TheIncredibles("Incredibles", incredible_members)
    incredibles.incredible_presentation()


    incredibles.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='BabyJack')
    incredibles.incredible_presentation()
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat("Mimi", 2)
cat2 = Cat("Tom", 3)
cat3 = Cat("Jerry", 1)

cat_list = [cat1, cat2, cat3]

def getOldestCat(cats):
    oldCat = cats[0]
    for cat in cats:
        if cat.age > oldCat.age:
            oldCat = cat
    return oldCat

oldest_cat = getOldestCat(cat_list)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")


class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * 3.14 * self.radius
    
    def describe(self):
        print("A circle is the set" \
        " of all points in a plane that are a " \
        "fixed distance from a center point.")

ex = Circle(5)
print(ex.get_area())
print(ex.get_perimeter())
ex.describe()
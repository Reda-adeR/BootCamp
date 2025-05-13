
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if (not radius and not diameter) or radius and diameter:
            raise ValueError("Bad instantiation") 
        self.radius = radius
        self.diameter = diameter

    def compute_area(self):
        import math
        r = self.radius if self.radius else self.diameter/2
        area = round(math.pi * pow(r, 2), 2)
        print("py ",area)
        return area
    
    def __str__(self):
        rad =  f"Radius   of this circle is : {self.radius}"
        diam = f"diameter of this circle is : {self.diameter}"
        return rad + '\n' + diam

    def transform(self, obj1, obj2):
        selfRad = obj1.radius if obj1.radius else obj1.diameter / 2
        objRad  = obj2.radius  if obj2.radius  else obj2.diameter  / 2
        return (selfRad, objRad)

    def __add__(self, obj):
        objs = self.transform(self, obj)
        return Circle(objs[0] + objs[1])
    
    def __gt__(self,obj):
        objs = self.transform(self, obj)
        return objs[0] > objs[1]
    
    def __eq__(self,obj):
        objs = self.transform(self, obj)
        return objs[0] == objs[1]
    
    def __float__(self):
        rad = self.radius if self.radius else self.diameter / 2
        return float(rad)


gg1 = Circle(3)
gg2 = Circle(5)
gg3 = Circle(7)
gg5 = Circle(9)
gg6 = Circle(10)

radii = [gg1,gg2,gg3,gg5,gg6]

turtle.penup()
x = -150

for r in radii:
    turtle.goto(x, 0 - float(r))
    turtle.pendown()
    turtle.circle(float(r))
    turtle.penup()
    x += 2 * float(r) + 10  # Move to the right for next circle

turtle.done()
    

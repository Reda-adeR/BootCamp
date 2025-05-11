
default_menu = [
    {"name" : "Pizza", "price": 10, "spice" : "A", "gluten" : False},
    {"name" : "Pasta", "price": 8, "spice" : "B", "gluten" : True},
    {"name" : "Salad", "price": 5, "spice" : "C", "gluten" : False},
    {"name" : "Soup", "price": 6, "spice" : "D", "gluten" : True},
    {"name" : "Steak", "price": 15, "spice" : "E", "gluten" : False},
]

class MenuManager:
    def __init__(self, menu=default_menu):
        self.menu = menu

    def add_item(self, name, price, spice, gluten):
        if name in [item["name"] for item in self.menu]:
            print("Chef the item is already in the menu")
            return
        dict = {"name" : name, "price": price, "spice" : spice, "gluten" : gluten}
        self.menu.append(dict)

    def update_item(self, name, price, spice, gluten):
        for elem in self.menu:
            if name in elem.values():
                elem["price"] = price
                elem["spice"] = spice
                elem["gluten"] = gluten
                return
        print("UPDATE : Chef the item is not in the menu")

    def show_menu(self):
        for elem in self.menu:
            print(f"Name: {elem['name']}, Price: {elem['price']}, Spice: {elem['spice']}, Gluten: {elem['gluten']}")

    def remove_item(self,name):
        for elem in self.menu:
            if name in elem.values():
                self.menu.remove(elem)
                self.show_menu()
                return
        print("REMOVE : Chef the item is not in the menu")


gg = MenuManager()
gg.update_item("Pizza", 10, "A", False)
gg.update_item("Pizza", 10, "A", False)
gg.remove_item("Pizza")

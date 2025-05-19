from menu_item import MenuItem
from menu_manager import MenuManager


class Editor:
    def __init__(self):
        self.items = []
        self.is_up_to_date = False

    def show_user_menu(self):
        print("Welcome To your Menu manager")
        print("-------- > Choose an Action : ")
        dict = { "C" : self.addItem, "R" : self.viewItem, "U" : self.updateItem ,
                "D" : self.removeItem, "S" : self.showMenu, "X" : self.exitMenu }
        while 1:    
            print()
            print(  "Create an Item (C)\n" \
                    "Read   an Item (R)\n" \
                    "Update an Item (U)\n" \
                    "Delete an Item (D)\n" \
                    "Show the Menu  (S)\n" \
                    "EXIT MENU      (X)")
            while 1:
                choice = input("__ : ")
                if choice.upper() in dict:
                    break

            dict[choice.upper()]()

    def addItem(self):
        print()
        name  = input("Enter item's Name  :  ")
        price = input("Enter item's price :  ")
        menu = MenuItem(name, int(price))
        menu.save()
        self.is_up_to_date = False

    def viewItem(self):
        print()
        selection = input("Enter the Name of the Item to view : ")
        menu = MenuManager()
        res = menu.get_by_name([selection])
        self.print_items(res)
        
    def updateItem(self):
        print()
        id    = input("Enter the ID of the item to update : ")
        name  = input("Enter New  item's Name  :  ")
        price = input("Enter New  item's price :  ")
        menu = MenuItem()
        menu.update(int(id), name, int(price))
        self.is_up_to_date = False

    def removeItem(self):
        print()
        id    = input("Enter the ID of the item to remove : ")
        menu = MenuItem()
        menu.delete([int(id)])
        self.is_up_to_date = False

    def print_items(self, items):
        print()
        print(f"{'ID':<5} {'Name':<20} {'Price':>10}")
        print("-" * 40)
        for item in items:
            print(f"{item[0]:<5} {item[1]:<20} {item[2]:>10.2f}")

    def showMenu(self):
        if not self.is_up_to_date:
            menu = MenuManager()
            self.items = menu.all_items()
            self.is_up_to_date = True
        self.print_items(self.items)
        # print(*self.items, sep="\n")

    def exitMenu(self):
        exit()

ls = Editor()
ls.show_user_menu()
from menu_item import MenuItem
from menu_manager import MenuManager


class Editor:
    def __init__(self):
        self.items = []
        self.is_up_to_date = False

    def show_user_menu(self):
        print("Welcome To your Menu manager")
        print("Choose an Action : ")
        while 1:    
            print(  "Create an Item (C)\n" \
                    "Read   an Item (R)\n" \
                    "Update an Item (U)\n" \
                    "Delete an Item (D)\n" \
                    "Show the Menu  (S)\n" \
                    "EXIT MENU      (X)")
            dict = { "C" : self.addItem, "R" : self.viewItem, "U" : self.updateItem ,
                    "D" : self.removeItem, "S" : self.showMenu, "X" : self.exitMenu }
            while 1:
                choice = input("__ : ")
                if choice in dict:
                    break

            dict[choice]()

    def addItem(self):
        name  = input("Enter item's Name  :  ")
        price = input("Enter item's price :  ")
        menu = MenuItem(name, int(price))
        menu.save()
        self.is_up_to_date = False

    def viewItem(self):
        pass
        
    def updateItem(self):
        pass

    def removeItem(self):
        pass

    def showMenu(self):
        if not self.is_up_to_date:
            menu = MenuManager()
            self.items = menu.all_items()
            self.is_up_to_date = True
        print("_*_*_*_*_*_*_*_")
        print()
        print(*self.items, sep="\n")
        print()
        print("_*_*_*_*_*_*_*_")

    def exitMenu(self):
        exit()

ls = Editor()
ls.show_user_menu()
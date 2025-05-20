from menu_manager import MenuManager

STR_INPUT_NAME =  "Enter  Name : "
STR_INPUT_PRICE = "Enter Price : "
STR_INPUT_ID = "Enter ID : "

def show_user_menu(obj):
    print("Welcome To your Menu manager")
    print("-------- > Choose an Action : ")
    dict = { "C" : obj.addItem, "R" : obj.viewItem, "U" : obj.updateItem ,
            "D" : obj.removeItem, "S" : obj.showMenu, "X" : obj.exitMenu }
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



class Editor(MenuManager):
    def __init__(self):
        super().__init__()
        self.items = []
        self.is_up_to_date = False

    def inputer(self, str):
        print()
        return input(str)

    def addItem(self):
        name  = self.inputer(STR_INPUT_NAME)
        price = self.inputer(STR_INPUT_PRICE)
        self.save(name, int(price))
        self.is_up_to_date = False

    def viewItem(self):
        selection = self.inputer(STR_INPUT_NAME)
        item = self.get_by_name([selection])
        self.print_items( item )
        
    def updateItem(self):
        id    = input(STR_INPUT_ID)
        name  = input(STR_INPUT_NAME)
        price = input(STR_INPUT_PRICE)
        self.update(int(id), name, int(price))
        self.is_up_to_date = False

    def removeItem(self):
        id    = input(STR_INPUT_ID)
        self.delete([int(id)])
        self.is_up_to_date = False

    def print_items(self, items):
        print(f"{'ID':<5} {'Name':<20} {'Price':>10}")
        print("-" * 40)
        for item in items:
            print(f"{item[0]:<5} {item[1]:<20} {item[2]:>10.2f}")

    def showMenu(self):
        if not self.is_up_to_date:
            self.items = self.all_items()
            self.is_up_to_date = True
        self.print_items(self.items)

    def exitMenu(self):
        exit()

ls = Editor()
show_user_menu(ls)
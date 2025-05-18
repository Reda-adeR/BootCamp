
from connector import Connector

class MenuManager:
    def __init__(self):
        self.db = Connector()

    def manage_query(self, query):
        self.db.connect()
        res = self.db.run_query(query, True)
        self.db.disconnect()
        return res

    def get_by_name(self, names):
        if names:
            ns = ["%s"] * len(names)
            query = f"SELECT * FROM menu_items WHERE item_name IN ({', '.join(ns)});"
            res = self.manage_query([query, tuple(names)])
            print("ITEMS REQUESTED : ")
            print(*res, sep='\n')
        # SELECT * FROM menu_items WHERE item_name IN ()

    def all_items(self):
        query = f"SELECT * FROM menu_items;"
        res = self.manage_query([query])
        print("ALL ITEMS")
        # print(*res, sep='\n')
        return res


if __name__ == "__main__":

    gg = MenuManager()

    gg.all_items()

# gg.get_by_name(["couscous"])




        
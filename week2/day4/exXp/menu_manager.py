
from connector import Connector
from menu_item import MenuItem


class MenuManager(MenuItem):
    def __init__(self):
        super().__init__()
        # self.db = Connector()

    def manage_query2(self, query):
        self.connect()
        res = self.run_query(query, True)
        self.disconnect()
        return res

    def get_by_name(self, names):
        if names:
            ns = ["%s"] * len(names)
            query = f"SELECT * FROM menu_items WHERE item_name IN ({', '.join(ns)});"
            res = self.manage_query2([query, tuple(names)])
            return res
        # SELECT * FROM menu_items WHERE item_name IN ()

    def all_items(self):
        query = f"SELECT * FROM menu_items;"
        res = self.manage_query2([query])
        return res


if __name__ == "__main__":

    gg = MenuManager()

    print(gg.all_items())

# gg.get_by_name(["couscous"])




        
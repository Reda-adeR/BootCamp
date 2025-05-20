

from connector import Connector

class MenuItem(Connector):
    def __init__(self):
        super().__init__()

    def manage_query1(self, query, fetch):
        self.connect()
        res = self.run_query(query, fetch)
        self.disconnect()
        if fetch : return res

    def save(self, name, price):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s);"
        self.manage_query1([query, (name, price)], False)
        print("added successfully")

    def delete(self, id):
        if id:
            ids = ["%s"] * len(id)
            query = f"DELETE FROM menu_items WHERE item_id IN ({', '.join(ids)}) RETURNING *;"
            res = self.manage_query1([query, tuple(id)], True)
            if res:
                print(*res, sep='\n')
                print("deleted successfully")

    def update(self, id, name=None, price=None):
        updates = []
        params = []

        def helper(str, element):
            if element:
                updates.append(str)
                params.append(element)

        helper("item_name = %s", name)
        helper("item_price = %s", price)

        if not updates:
            return

        query = f"UPDATE menu_items SET {', '.join(updates)} WHERE item_id = %s"
        params.append(id)
        self.manage_query1([query, tuple(params)], False)
        print("updated successfully")
        # cursor.execute(query, tuple(params))




if __name__ == "__main__":
    gg = MenuItem("burger", 100)

    # gg.save()
    # gg.delete([1,2])
    gg.update(5, "couscous", 1800)


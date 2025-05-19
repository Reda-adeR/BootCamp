

from connector import Connector

class MenuItem:
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price
        self.db = Connector()

    def manage_query(self, query, fetch):
        self.db.connect()
        res = self.db.run_query(query, fetch)
        self.db.disconnect()
        if fetch : return res

    def save(self):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s);"
        self.manage_query([query, (self.name, self.price)], False)
        print("added successfully")

    def delete(self, id):
        if id:
            ids = ["%s"] * len(id)
            query = f"DELETE FROM menu_items WHERE item_id IN ({', '.join(ids)}) RETURNING *;"
            res = self.manage_query([query, tuple(id)], True)
            if res:
                print(*res, sep='\n')
                print("deleted successfully")

    def update(self, id, name=None, price=None):
        updates = []
        params = []

        if name:
            updates.append("item_name = %s")
            params.append(name)
            self.name = name

        if price:
            updates.append("item_price = %s")
            params.append(price)
            self.price = price

        if not updates:
            return

        query = f"UPDATE menu_items SET {', '.join(updates)} WHERE item_id = %s"
        params.append(id)
        self.manage_query([query, tuple(params)], False)
        print("updated successfully")
        # cursor.execute(query, tuple(params))




if __name__ == "__main__":
    gg = MenuItem("burger", 100)

    # gg.save()
    # gg.delete([1,2])
    gg.update(5, "couscous", 1800)


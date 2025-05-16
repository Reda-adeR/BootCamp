
import psycopg2
from psycopg2 import OperationalError

hostName = 'localhost'
userName = 'postgres'
psw      = '123'
db       = 'bootcamp'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host        = hostName,
                user        = userName,
                password    = psw,
                dbname      = db
            )
            print("connected to db")
        except OperationalError as e:
            print("Connection Failed : ", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("disconnected")

    def manage_query(self, query):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(query[0]) if len(query) < 2 else cursor.execute(query[0], query[1])
        cursor.connection.commit()
        self.disconnect()

    def save(self):
        # self.connect()
        # cursor = self.connection.cursor()
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s);"
        # cursor.execute(query, (self.name, self.price))
        self.manage_query([query, (self.name, self.price)])
        print("added")
        # self.connection.commit()
        # print("saved")
        # self.disconnect()

    def delete(self, id):
        if id:
            ids = ["%s"] * len(id)
            query = f"DELETE FROM menu_items WHERE item_id IN ({', '.join(ids)});"
            self.manage_query([query, tuple(id)])
            print(', '.join(str(id) for i in id)," : are deleted")

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
        self.manage_query([query, tuple(params)])
        # cursor.execute(query, tuple(params))



gg = MenuItem("burger", 100)

# gg.save()
# gg.delete([1,2])
gg.update(5, "pizza", 800)


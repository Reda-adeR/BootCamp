
import psycopg2
from psycopg2 import OperationalError


hostName = 'localhost'
userName = 'postgres'
psw      = '123'
db       = 'bootcamp'

class Connector:
    def __init__(self):
        self.connection = None

    def connect(self):
        if not self.connection:
            try:
                self.connection = psycopg2.connect(
                    host        = hostName,
                    user        = userName,
                    password    = psw,
                    dbname      = db
                )
                print("connected to db")
                return self.connection
            except OperationalError as e:
                print("Connection Failed : ", e)
        else:
            return self.connection

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("disconnected")

    def run_query(self, query, fetch):
        if self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query[0]) if len(query) < 2 else cursor.execute(query[0], query[1])
            cursor.connection.commit()
            if fetch:
                res = cursor.fetchall()
                # print(res)
                return res

    # def get_data(self, query):
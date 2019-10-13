import psycopg2
import backendSQL as baseData


class ModelShop(object):

    def __init__(self):
        self._connection = self.connect_to_db()
        self._tableName = "Shop"

    @property
    def connection(self):
        return self._connection

    @staticmethod
    def connect_to_db():
        connection = psycopg2.connect(user="postgres", password="password", host="127.0.0.1", port="5432",
                                      database="Shops")
        return connection

    def disconnect_from_db(self):
        if self.connection is not None:
            self.connection.close()
            print("PostgresSQL connection is closed")

    def create_shop(self, name, street):
        print("4")
        baseData.insert_one(self.connection, name, street)

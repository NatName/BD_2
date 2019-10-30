import psycopg2
from BD_2 import backendSQL as baseData
from BD_2.additional import Additional


class Model(object):
    def __init__(self):
        self._connection = self.connect_to_db()

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


class ModelShop(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Shop"

    @property
    def tableName(self):
        return self._tableName

    def create_shop(self, name, street):
        baseData.insert_one_shop(self.connection, name, street)

    def create_many_shops(self, count):
        baseData.insert_many_random_shops(self.connection, count)

    def update_shop(self, shopId, name, street):
        try:
            assert Additional.findExistingId(self.connection, self.tableName, shopId), \
                '\033[91m id isn\'t exist \033[0m '
            baseData.update_one_shop(
                self.connection, shopId, name, street)
            return True
        except Exception as err:
            print(err)
            return False

    def read_shops(self):
        return baseData.select_all(self.connection, self._tableName)

    def read_shop(self, shopId):
        return baseData.select_one(self.connection, self._tableName, shopId)

    def delete_shop(self, shopId):
        try:
            assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, shopId), \
                '\033[91m shop id bind with order \033[0m'
            assert Additional.findExistingId(self.connection, self.tableName, shopId), \
                '\033[91m id isn\'t exist \033[0m'
            baseData.delete_one(self.connection, shopId, self.tableName)
            return True
        except Exception as err:
            print(err)
            return False


class ModelCustomer(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Customer"

    @property
    def tableName(self):
        return self._tableName

    def create_customer(self, name, phone, sex):
        try:
            assert (sex == "male" or sex == "female"), \
                '\033[91m sex isn\'t exist. You must input male or female \033[0m'
            baseData.insert_one_customer(self.connection, name, phone, sex)
            return True
        except Exception as err:
            print(err)
            return False

    def create_many_customers(self, count):
        baseData.insert_many_random_customers(self.connection, count)

    def update_customer(self, customerId, name, phone, sex):
        try:
            assert (sex == "male" or sex == "female"), \
                '\033[91m sex isn\'t exist. You must input male or female \033[0m'
            assert Additional.findExistingId(self.connection, self.tableName, customerId), \
                '\033[91m id isn\'t exist \033[0m '
            baseData.update_one_customer(
                self.connection, customerId, name, phone, sex)
            return True
        except Exception as err:
            print(err)
            return False

    def read_customers(self):
        return baseData.select_all(self.connection, self._tableName)

    def read_customer(self, customerId):
        return baseData.select_one(self.connection, self._tableName, customerId)

    def delete_customer(self, customerId):
        try:
            assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, customerId),\
                '\033[91m You don\'t delete customer, because this customer bind with order \033[0m'
            assert Additional.findExistingId(self.connection, self.tableName, customerId), \
                '\033[91m id isn\'t exist \033[0m'
            baseData.delete_one(self.connection, customerId, self.tableName)
            return True
        except Exception as err:
            print(err)
            return False


class ModelItem(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Item"

    @property
    def tableName(self):
        return self._tableName

    def create_item(self, name, price, quantity, color, material, description):
        try:
            assert price > 0, '\033[91m price must be more zero \033[0m'
            assert quantity > 0, '\033[91m quantity must be > 0 \033[0m '
            baseData.insert_one_item(self.connection, name, price, quantity, color, material, description)
            return True
        except Exception as err:
            print(err)
            return False

    def create_many_items(self, count):
        baseData.insert_many_random_items(self.connection, count)

    def read_items(self, value, word=None):
        if word and value == 1:
            strWord = Additional.addLogicOperation(word)
            return Additional.findWordInText(self.connection, strWord)
        elif value == 2:
            return Additional.findTextWithoutWord(self.connection, word)
        return baseData.select_all(self.connection, self.tableName)

    def read_item(self, itemId):
        return baseData.select_one(self.connection, self.tableName, itemId)

    def update_item(self, itemId, name, price, quantity, color, material, description):
        try:
            assert price > 0, '\033[91m price must be more zero \033[0m'
            assert quantity > 0, '\033[91m quantity must be > 0 \033[0m'
            assert Additional.findExistingId(self.connection, self.tableName, itemId), \
                '\033[91m id isn\'t exist \033[0m'
            baseData.update_one_item(
                self.connection, itemId, name, price, quantity, color, material, description)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_item(self, itemId):
        try:
            assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, itemId), \
                '\033[91m item id bind with order \033[0m'
            assert Additional.findExistingId(self.connection, self.tableName, itemId), \
                '\033[91m id isn\'t exist \033[0m'
            baseData.delete_one(self.connection, itemId, self.tableName)
            return True
        except Exception as err:
            print(err)
            return False


class ModelOrder(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Order"

    @property
    def tableName(self):
        return self._tableName

    def create_order(self, itemId, shopId, customerId, date):
        try:
            assert Additional.findExistingId(self.connection, "Item", itemId), '\033[91m item id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Shop", shopId), '\033[91m shop id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Customer", customerId), \
                '\033[91m customer id isn\'t exist \033[0m'
            baseData.insert_one_order(self.connection, itemId, shopId, customerId, date)
            return True
        except Exception as err:
            print(err)
            return False

    def create_many_orders(self, count):
        try:
            itemId = Additional.findExistRow(self.connection, "Item")
            shopId = Additional.findExistRow(self.connection, "Shop")
            customerId = Additional.findExistRow(self.connection, "Customer")
            assert Additional.findExistingId(self.connection, "Item", itemId), '\033[91m item id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Shop", shopId), '\033[91m shop id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Customer", customerId), \
                '\033[91m customer id isn\'t exist \033[0m'
            baseData.insert_many_random_orders(self.connection, count, itemId, customerId, shopId)
            return True
        except Exception as err:
            print(err)
            return False

    def read_orders(self):
        return baseData.select_all(self.connection, self.tableName)

    def read_order(self, orderId):
        return baseData.select_one(self.connection, self.tableName, orderId)

    def read_order_another_table(self, first, second=None):
        return Additional.findRowBetweenNumbers(self.connection, first, second)

    def read_order_itemName(self, name):
        return Additional.findItemName(self.connection, name)

    def update_order(self, orderId, itemId, shopId, customerId, date):
        try:
            assert Additional.findExistingId(self.connection, self.tableName, orderId), \
                '\033[91m id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Item", itemId), '\033[91m item id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Shop", shopId), '\033[91m shop id isn\'t exist \033[0m'
            assert Additional.findExistingId(self.connection, "Customer", customerId), \
                '\033[91m customer id isn\'t exist \033[0m'
            baseData.update_one_order(
                self.connection, orderId, itemId, shopId, customerId, date)
            return True
        except Exception as err:
            print(err)
            return False

    def delete_order(self, orderId):
        try:
            assert Additional.findExistingId(self.connection, self.tableName, orderId), \
                '\033[91m id isn\'t exist \033[0m'
            baseData.delete_one(self.connection, orderId, self.tableName)
            return True
        except Exception as err:
            print(err)
            return False

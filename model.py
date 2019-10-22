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
        shopId = Additional.findId(self.connection, self.tableName)
        assert not Additional.findExistingId(self.connection, self.tableName, shopId), 'id must be unique'
        baseData.insert_one_shop(self.connection, name, street)

    def create_many_shops(self, count):
        baseData.insert_many_random_shops(self.connection, count)

    def update_shop(self, shopId, name, street):
        assert Additional.findExistingId(self.connection, self.tableName, shopId), 'id isn\'t exist'
        baseData.update_one_shop(
            self.connection, shopId, name, street)

    def read_shops(self):
        return baseData.select_all(self.connection, self._tableName)

    def read_shop(self, shopId):
        return baseData.select_one(self.connection, self._tableName, shopId)

    def delete_shop(self, shopId):
        assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, shopId), 'shop id ' \
                                                                                                 'bind with order '
        assert Additional.findExistingId(self.connection, self.tableName, shopId), 'id isn\'t exist'
        baseData.delete_one(self.connection, shopId, self.tableName)


class ModelCustomer(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Customer"

    @property
    def tableName(self):
        return self._tableName

    def create_customer(self, name, phone, sex):
        customerId = Additional.findId(self.connection, self.tableName)
        assert (sex == "male" or sex == "female"), 'sex isn\'t exist. You must input male or female'
        assert not Additional.findExistingId(self.connection, self.tableName, customerId), 'id must be unique'
        baseData.insert_one_customer(self.connection, name, phone, sex)

    def create_many_customers(self, count):
        baseData.insert_many_random_customers(self.connection, count)

    def update_customer(self, customerId, name, phone, sex):
        assert (sex == "male" or sex == "female"), 'sex isn\'t exist. You must input male or female'
        assert Additional.findExistingId(self.connection, self.tableName, customerId), 'id isn\'t exist'
        baseData.update_one_customer(
            self.connection, customerId, name, phone, sex)

    def read_customers(self):
        return baseData.select_all(self.connection, self._tableName)

    def read_customer(self, customerId):
        return baseData.select_one(self.connection, self._tableName, customerId)

    def delete_customer(self, customerId):
        assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, customerId), 'customer id ' \
                                                                                                     'bind with order '
        assert Additional.findExistingId(self.connection, self.tableName, customerId), 'id isn\'t exist'
        baseData.delete_one(self.connection, customerId, self.tableName)


class ModelItem(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Item"

    @property
    def tableName(self):
        return self._tableName

    def create_item(self, name, price, quantity, color, material, description):
        assert price > 0, 'price must be more zero'
        assert quantity > 0, 'quantity must be > 0'
        baseData.insert_one_item(self.connection, name, price, quantity, color, material, description)

    def create_many_items(self, count):
        baseData.insert_many_random_items(self.connection, count)

    def read_items(self, word=None):
        if word:
            return Additional.findWordInText(self.connection, word)
        return baseData.select_all(self.connection, self.tableName)

    def read_item(self, itemId):
        return baseData.select_one(self.connection, self.tableName, itemId)

    def update_item(self, itemId, name, price, quantity, color, material, description):
        assert price > 0, 'price must be more zero'
        assert quantity > 0, 'quantity must be > 0'
        assert Additional.findExistingId(self.connection, self.tableName, itemId), 'id isn\'t exist'
        baseData.update_one_item(
            self.connection, itemId, name, price, quantity, color, material, description)

    def delete_item(self, itemId):
        assert not Additional.findExistingIdOrderTable(self.connection, self.tableName, itemId), 'item id bind with ' \
                                                                                                 'order '
        assert Additional.findExistingId(self.connection, self.tableName, itemId), 'id isn\'t exist'
        baseData.delete_one(self.connection, itemId, self.tableName)


class ModelOrder(Model):

    def __init__(self):
        super().__init__()
        self._tableName = "Order"

    @property
    def tableName(self):
        return self._tableName

    def create_order(self, itemId, shopId, customerId, date):
        assert Additional.findExistingId(self.connection, "Item", itemId), 'item id isn\'t exist'
        assert Additional.findExistingId(self.connection, "Shop", shopId), 'shop id isn\'t exist'
        assert Additional.findExistingId(self.connection, "Customer", customerId), 'customer id isn\'t exist'
        baseData.insert_one_order(self.connection, itemId, shopId, customerId, date)

    def create_many_orders(self, count):
        itemId = Additional.findExistRow(self.connection, "Item")
        shopId = Additional.findExistRow(self.connection, "Shop")
        customerId = Additional.findExistRow(self.connection, "Customer")
        baseData.insert_many_random_orders(self.connection, count, itemId, customerId, shopId)

    def read_orders(self):
        return baseData.select_all(self.connection, self.tableName)

    def read_order(self, orderId):
        return baseData.select_one(self.connection, self.tableName, orderId)

    def read_order_another_table(self, first, second=None, anyName=None):
        return Additional.findRowBetweenNumbers(self.connection, first, second, anyName)

    def update_order(self, orderId, itemId, shopId, customerId, date):
        assert Additional.findExistingId(self.connection, self.tableName, orderId), 'id isn\'t exist'
        baseData.update_one_order(
            self.connection, orderId, itemId, shopId, customerId, date)

    def delete_order(self, orderId):
        assert Additional.findExistingId(self.connection, self.tableName, orderId), 'id isn\'t exist'
        currentOrder = self.read_order(orderId)
        print(currentOrder)
        baseData.delete_one(self.connection, orderId, self.tableName)

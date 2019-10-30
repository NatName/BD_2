from BD_2.isTrueData import Check
from BD_2.inputData import Input


class ControllerShop(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def insert_shop(self, shop):
        try:
            shop = Input.input_update_shop(shop)
            assert Check.isExistAllOptionShop(shop), '\033[91m you don\'t add all needed shop\'s option \033[0m'
            self.model.create_shop(shop['name'], shop['street'])
            self.view.display_stored(shop['name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_shops(self):
        try:
            count = Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_shops(count)
            self.view.display_many_stored(count, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_shops(self):
        items = self.model.read_shops()
        self.view.show_list_shops(items)

    def show_shop(self):
        shopId = Input.input_id(self.model.tableName)
        shop = self.model.read_shop(shopId)
        self.view.show_list_shops(shop)

    def update_shop(self, shop):
        shopId = Input.input_id(self.model.tableName)
        shop = Input.input_update_shop(shop)
        older = self.model.read_shop(shopId)
        newShop = Check.updateShop(shop, older)
        check = self.model.update_shop(shopId, newShop['name'], newShop['street'])
        if check:
            self.view.display_shop_updated(shopId, older[0][1], older[0][2], newShop['name'], newShop['street'])

    def delete_shop(self):
        shopId = Input.input_id(self.model.tableName)
        check = self.model.delete_shop(shopId)
        if check:
            self.view.display_deletion(shopId, self.model.tableName)


class ControllerCustomer(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def insert_customer(self, customer):
        try:
            customer = Input.input_update_customer(customer)
            assert Check.isExistAllOptionCustomer(customer), \
                '\033[91m you don\'t add all needed customer\'s option \033[0m '
            check = self.model.create_customer(customer['name'], customer['phone'], customer['sex'])
            if check:
                self.view.display_stored(customer['name'], self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_customers(self):
        try:
            count = Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_customers(count)
            self.view.display_many_stored(count, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_customers(self):
        items = self.model.read_customers()
        self.view.show_list_customers(items)

    def show_customer(self):
        customerId = Input.input_id(self.model.tableName)
        customer = self.model.read_customer(customerId)
        self.view.show_list_customers(customer)

    def update_customer(self, customer):
        customerId = Input.input_id(self.model.tableName)
        customer = Input.input_update_customer(customer)
        older = self.model.read_customer(customerId)
        newCustomer = Check.updateCustomer(customer, older)
        check = self.model.update_customer(customerId, newCustomer['name'], newCustomer['phone'], newCustomer['sex'])
        if check:
            self.view.display_customer_updated(customerId, older[0][1], older[0][2], older[0][3],
                                               newCustomer['name'], newCustomer['phone'], newCustomer['sex'])

    def delete_customer(self):
        customerId = Input.input_id(self.model.tableName)
        check = self.model.delete_customer(customerId)
        if check:
            self.view.display_deletion(customerId, self.model.tableName)


class ControllerItem(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def insert_item(self, items):
        try:
            items = Input.input_update_item(items)
            description = None
            assert Check.isExistAllOptionItem(items), '\033[91m you don\'t add all needed item\'s option \033[0m '
            if 'description' in items:
                description = items['description']
            check = self.model.create_item(items['name'], items['price'], items['quantity'], items['color'],
                                           items['material'], description)
            if check:
                self.view.display_stored('name', self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_items(self):
        try:
            count = Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            self.model.create_many_items(count)
            self.view.display_many_stored(count, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_items(self, value):
        word = Input.input_words()
        items = self.model.read_items(value, word)
        self.view.show_list_items(items, word)

    def show_item(self):
        itemId = Input.input_id(self.model.tableName)
        items = self.model.read_item(itemId)
        self.view.show_list_items(items, None)

    def update_item(self, item):
        itemId = Input.input_id(self.model.tableName)
        item = Input.input_update_item(item)
        older = self.model.read_item(itemId)
        item = Check.updateItem(item, older)
        check = self.model.update_item(itemId, item['name'], item['price'], item['quantity'],
                                       item['color'], item['material'], item['description'])
        if check:
            self.view.display_item_updated(itemId, older, item['name'], item['price'], item['quantity'],
                                           item['color'], item['material'], item['description'])

    def delete_item(self):
        itemId = Input.input_id(self.model.tableName)
        check = self.model.delete_item(itemId)
        if check:
            self.view.display_deletion(itemId, self.model.tableName)


class ControllerOrder(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view()

    def insert_order(self, order):
        try:
            order = Input.input_update_order(order)
            assert Check.isExistAllOptionOrder(order), \
                '\033[91m  you don\'t add all needed order\'s option \033[0m'
            check = self.model.create_order(order['itemId'], order['shopId'], order['customerId'], order['date'])
            if check:
                self.view.display_stored("", self.model.tableName)
        except Exception as err:
            print(err)

    def insert_many_orders(self):
        try:
            count = Input.input_count()
            assert count > 1, '\033[91m count must be more one \033[0m'
            check = self.model.create_many_orders(count)
            if check:
                self.view.display_many_stored(count, self.model.tableName)
        except Exception as err:
            print(err)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_orders(self):
        orders = self.model.read_orders()
        self.view.show_list_orders(orders)

    def show_order_by_quantity(self):
        try:
            values = Input.input_two_value()
            assert values[0] <= values[1], '\033[91m first value must be less than second value\033[0m'
            items = self.model.read_order_another_table(values[0], values[1])
            self.view.show_list_items_orders(items, "ItemQuantity  |")
        except Exception as err:
            print(err)
            return False

    def show_order_by_itemName(self):
        name = Input.input_name()
        items = self.model.read_order_itemName(name)
        self.view.show_list_items_orders(items, "ItemName          |")

    def show_order(self):
        orderId = Input.input_id(self.model.tableName)
        order = self.model.read_order(orderId)
        self.view.show_list_orders(order)

    def update_order(self, order):
        orderId = Input.input_id(self.model.tableName)
        order = Input.input_update_order(order)
        older = self.model.read_order(orderId)
        newOrder = Check.updateOrder(order, older)
        check = self.model.update_order(orderId, newOrder['itemId'], newOrder['shopId'], newOrder['customerId'],
                                        newOrder['date'])
        if check:
            self.view.display_order_updated(orderId, older, order['itemId'], order['shopId'],
                                            newOrder['customerId'], newOrder['date'])

    def delete_order(self):
        orderId = Input.input_id(self.model.tableName)
        check = self.model.delete_order(orderId)
        if check:
            self.view.display_deletion(orderId, self.model.tableName)

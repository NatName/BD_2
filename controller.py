from BD_2.additional import Additional


class ControllerShop(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view

    def insert_shop(self, shop):
        assert Additional.isExistAllOptionShop(shop), 'you don\'t add all needed shop\'s option'
        self.model.create_shop(shop['name'], shop['street'])
        self.view.display_stored(shop['name'], self.model.tableName)

    def insert_many_shops(self, count):
        self.model.create_many_shops(count)
        self.view.display_many_stored(count, self.model.tableName)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_shops(self):
        items = self.model.read_shops()
        self.view.show_list_shops(items)

    def show_shop(self, shopId):
        items = self.model.read_shop(shopId)
        self.view.show_list_shops(items)

    def update_shop(self, shopId, shop):
        older = self.model.read_shop(shopId)
        newShop = Additional.updateShop(shop, older)
        self.model.update_shop(shopId, newShop['name'], newShop['street'])
        self.view.display_shop_updated(shopId, older[0][1], older[0][2], newShop['name'], newShop['street'])

    def delete_shop(self, shopId):
        self.model.delete_shop(shopId)
        self.view.display_deletion(shopId, self.model.tableName)


class ControllerCustomer(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view

    def insert_customer(self, customer):
        assert Additional.isExistAllOptionCustomer(customer), 'you don\'t add all needed customer\'s option'
        self.model.create_customer(customer['name'], customer['phone'], customer['sex'])
        self.view.display_stored(customer['name'], self.model.tableName)

    def insert_many_customers(self, count):
        self.model.create_many_customers(count)
        self.view.display_many_stored(count, self.model.tableName)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_customers(self):
        items = self.model.read_customers()
        self.view.show_list_customers(items)

    def show_customer(self, customerId):
        items = self.model.read_customer(customerId)
        self.view.show_list_customers(items)

    def update_customer(self, customerId, customer):
        older = self.model.read_customer(customerId)
        newCustomer = Additional.updateCustomer(customer, older)
        self.model.update_customer(customerId, newCustomer['name'], newCustomer['phone'], newCustomer['sex'])
        self.view.display_customer_updated(customerId, older[0][1], older[0][2], older[0][3],
                                           newCustomer['name'], newCustomer['phone'], newCustomer['sex'])

    def delete_customer(self, customerId):
        self.model.delete_customer(customerId)
        self.view.display_deletion(customerId, self.model.tableName)


class ControllerItem(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view

    def insert_item(self, items):
        description = None
        assert Additional.isExistAllOptionItem(items), 'you don\'t add all needed item\'s option'
        if 'description' in items:
            description = items['description']
        self.model.create_item(items['name'], items['price'], items['quantity'], items['color'],
                               items['material'], description)
        self.view.display_stored('name', self.model.tableName)

    def insert_many_items(self, count):
        self.model.create_many_items(count)
        self.view.display_many_stored(count, self.model.tableName)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_items(self, word=None):
        items = self.model.read_items(word)
        self.view.show_list_items(items, word)

    def show_item(self, itemId):
        items = self.model.read_item(itemId)
        self.view.show_list_items(items, None)

    def update_item(self, itemId, item):
        older = self.model.read_item(itemId)
        item = Additional.updateItem(item, older)
        self.model.update_item(itemId, item['name'], item['price'], item['quantity'],
                               item['color'], item['material'], item['description'])
        self.view.display_item_updated(itemId, older, item['name'], item['price'], item['quantity'],
                                       item['color'], item['material'], item['description'])

    def delete_item(self, itemId):
        self.model.delete_item(itemId)
        self.view.display_deletion(itemId, self.model.tableName)


class ControllerOrder(object):

    def __init__(self, model, view):
        self.model = model()
        self.view = view

    def insert_order(self, order):
        assert Additional.isExistAllOptionOrder(order), 'you don\'t add all needed order\'s option'
        self.model.create_order(order['itemId'], order['shopId'], order['customerId'], order['date'])
        self.view.display_stored("", self.model.tableName)

    def insert_many_orders(self, count):
        self.model.create_many_orders(count)
        self.view.display_many_stored(count, self.model.tableName)

    def disconnect(self):
        self.model.disconnect_from_db()
        self.view.delete_connection()

    def show_orders(self):
        orders = self.model.read_orders()
        self.view.show_list_orders(orders)

    def show_order_with_another_table(self, first, second=None, anyName=None):
        items = self.model.read_order_another_table(first, second, anyName)
        self.view.show_list_items_orders(items)

    def show_order(self, orderId):
        order = self.model.read_order(orderId)
        self.view.show_list_orders(order)

    def update_order(self, orderId, order):
        older = self.model.read_order(orderId)
        newOrder = Additional.updateOrder(order, older)
        self.model.update_order(orderId, newOrder['itemId'], newOrder['shopId'], newOrder['customerId'], newOrder['date'])
        self.view.display_order_updated(orderId, older, order['itemId'], order['shopId'],
                                        newOrder['customerId'], newOrder['date'])

    def delete_order(self, orderId):
        self.model.delete_order(orderId)
        self.view.display_deletion(orderId, self.model.tableName)

class Check(object):

    @staticmethod
    def isExistAllOptionCustomer(customer):
        if 'name' and 'sex' and 'phone' not in customer:
            return False
        return True

    @staticmethod
    def updateCustomer(customer, older):
        i = 0
        options = ['name', 'phone', 'sex']
        for key in options:
            i += 1
            if key not in customer:
                customer[key] = older[0][i]
        return customer

    @staticmethod
    def isExistAllOptionShop(shop):
        if 'name' and 'street' not in shop:
            return False
        return True

    @staticmethod
    def updateShop(shop, older):
        i = 0
        options = ['name', 'street']
        for key in options:
            i += 1
            if key not in shop:
                shop[key] = older[0][i]
        return shop

    @staticmethod
    def isExistAllOptionItem(items):
        if 'name' and 'price' and 'quantity' and 'color' and 'material' not in items:
            return False
        return True

    @staticmethod
    def updateItem(items, older):
        i = 0
        options = ['name', 'price', 'quantity', 'color', 'material', 'description']
        for key in options:
            i += 1
            if key not in items:
                items[key] = older[0][i]
        return items

    @staticmethod
    def isExistAllOptionOrder(order):
        if 'itemId' and 'shopId' and 'customerId' and 'date' not in order:
            return False
        return True

    @staticmethod
    def updateOrder(order, older):
        i = 0
        options = ['itemId', 'shopId', 'customerId', 'date']
        for key in options:
            i += 1
            if key not in order:
                order[key] = older[0][i]
        return order





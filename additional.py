import psycopg2


class Additional(object):

    @staticmethod
    def findExistRow(connection, tableName):
        cursor = connection.cursor()
        cursor.execute("""SELECT "{}Id" FROM public."{}" OFFSET floor(random()) LIMIT 1;"""
                       .format(tableName, tableName))
        value = cursor.fetchall()
        return value[0][0] + 1

    @staticmethod
    def findExistingId(connection, tableName, anyId):
        cursor = connection.cursor()
        cursor.execute("""SELECT \"{}Id\" FROM public.\"{}\" WHERE \"{}Id\"={};"""
                       .format(tableName, tableName, tableName, anyId))
        value = cursor.fetchall()
        return len(value) != 0

    @staticmethod
    def findExistingIdOrderTable(connection, tableName, anyId):
        cursor = connection.cursor()
        cursor.execute("""SELECT \"{}Id\" FROM public.\"Order\" WHERE \"{}Id\"={};"""
                       .format(tableName, tableName, anyId))
        value = cursor.fetchall()
        return len(value) != 0

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
    def findWordInText(connection, word):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM public."Item" WHERE "ItemDescriptions" LIKE '%{}%';"""
                       .format(word))
        value = cursor.fetchall()
        return value

    @staticmethod
    def findRowBetweenNumbers(connection, first, second, name):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM public."Order" INNER JOIN public."{}" ON "Order"."{}Id"="{}"."{}Id" WHERE  
                        "OrderId" BETWEEN {} AND {} AND "{}"."{}Id" BETWEEN {} AND {};"""
                       .format(name, name, name, name, first, second, name, name, first, second))
        value = cursor.fetchall()
        return value

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

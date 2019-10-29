import psycopg2


class Additional(object):

    @staticmethod
    def findExistRow(connection, tableName):
        cursor = connection.cursor()
        cursor.execute("""SELECT "{}Id" FROM public."{}" OFFSET floor(random()) LIMIT 1;"""
                       .format(tableName, tableName))
        value = cursor.fetchall()
        return value[0][0]

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
    def findWordInText(connection, words):
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM public."Item" WHERE to_tsvector("ItemDescriptions") @@ to_tsquery('{}');"""
                       .format(words))
        value = cursor.fetchall()
        return value

    @staticmethod
    def findRowBetweenNumbers(connection, first, second):
        cursor = connection.cursor()
        cursor.execute("""SELECT "OrderId", "CustomerId", "ShopId", "OrderDate", "Item"."ItemId",  "ItemQuantity" FROM public."Order" INNER JOIN public."Item" ON "Order"."ItemId"="Item"."ItemId" WHERE  
                        "ItemQuantity" BETWEEN {} AND {};"""
                       .format(first, second))
        value = cursor.fetchall()
        return value

    @staticmethod
    def findItemName(connection, name):
        cursor = connection.cursor()
        cursor.execute("""SELECT "OrderId", "CustomerId", "ShopId", "OrderDate", "Item"."ItemId",  "ItemName" FROM public."Order" INNER JOIN public."Item" ON "Order"."ItemId"="Item"."ItemId" WHERE  
                        "ItemName" LIKE '{}';"""
                       .format(name))
        value = cursor.fetchall()
        return value

    @staticmethod
    def addLogicOperation(word):
        word = word.strip().replace('and', '&').replace('or', '|')
        desc = word.split(' ')
        i = 0
        filterStr = list(filter(lambda x: x != '' and x != 'or' and x != 'and', desc))
        desc = ''
        while i < len(filterStr) - 1:
            if filterStr[i] == '|' or filterStr[i] == '&':
                desc += filterStr[i] + ' '
            elif filterStr[i+1] == '|' or filterStr[i+1] == '&':
                desc += filterStr[i] + ' '
            else:
                desc += filterStr[i] + ' & '
            i += 1
        desc += filterStr[i]
        return desc

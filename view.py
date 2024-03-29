class View(object):

    @staticmethod
    def show_list_shops(items):
        if items:
            print("----------------SHOPS------------------")
            print("|ShopId\t|", "ShopName     |", "ShopStreet   |")
            for row in items:
                print("|", row[0], "\t|", row[1], " " * (11 - len(row[1])), "|", row[2], " " * (11 - len(row[2])), "|")
            print("---------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def display_shop_updated(shopId, oldName, oldStreet, newName, newStreet):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} name: {} --> {}'
              .format(shopId, oldName, newName))
        print('Change {} street: {} --> {}'
              .format(shopId, oldStreet, newStreet))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def show_list_customers(items):
        if items:
            print("----------------CUSTOMERS----------------------------------------")
            print("|CustomerId\t|", "CustomerName\t|", "CustomerPhone      |", "CustomerSex  |")
            for row in items:
                print("|", row[0], "\t\t|", row[1], "\t|", row[2], " " * (17 - len(row[2])), "|", row[3],
                      " " * (10 - len(row[3])), "\t|")
            print("-----------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def display_customer_updated(shopId, oldName, oldPhone, oldSex, newName, newPhone, newSex):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} name: {} --> {}'
              .format(shopId, oldName, newName))
        print('Change {} phone: {} --> {}'
              .format(shopId, oldPhone, newPhone))
        print('Change {} sex: {} --> {}'
              .format(shopId, oldSex, newSex))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(itemId, old, name, price, quantity, color, material, description):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} name: {} --> {}'
              .format(itemId, old[0][1], name))
        print('Change {} price: {} --> {}'
              .format(itemId, old[0][2], price))
        print('Change {} quantity: {} --> {}'
              .format(itemId, old[0][3], quantity))
        print('Change {} color: {} --> {}'
              .format(itemId, old[0][4], color))
        print('Change {} material: {} --> {}'
              .format(itemId, old[0][5], material))
        print('Change {} description: {} --> {}'
              .format(itemId, old[0][6], description))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def show_list_items(items, word):
        if word:
            word = word.split(' ')
            filterWord = list(filter(lambda x: x != 'or' and x != '' and x != 'and', word))
        if items:
            print("------------------------------------ITEMS-----------------------------------------")
            print("|ItemId\t|", "ItemName    |", "ItemPrice   |", "ItemQuantity  |", "ItemColor   |",
                  "ItemMaterial  |",
                  "ItemDescriptions      |")
            for row in items:
                if word:
                    for rowWord in filterWord:
                        row = list(row)
                        row[6] = row[6].replace(rowWord, "\033[93m" + rowWord + "\033[0m")
                print("|", row[0], "\t|", row[1], " " * (10 - len(row[1])), "|", row[2], "\t|", row[3],
                      "\t\t\t|", row[4], " " * (10 - len(row[4])), "|", row[5], " " * (12 - len(row[5])),
                      "|", row[6], "|")
                print("----------------------------------------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def show_list_orders(orders):
        if orders:
            print("--------------------ORDERS------------------------")
            print("|OrderId|", "CustomerId|", "ItemId|", "ShopId|", "OrderDate  |")
            for row in orders:
                print("|", row[0], "\t|", row[1], "\t\t|", row[2], "\t|", row[3],
                      "\t|", row[4], "|")
            print("--------------------------------------------------")
        else:
            print("There is nothing with this id")

    @staticmethod
    def display_order_updated(orderId, old, itemId, shopId, customerId, date):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Change {} item: {} --> {}'
              .format(orderId, old[0][1], itemId))
        print('Change {} shop: {} --> {}'
              .format(orderId, old[0][2], shopId))
        print('Change {} customer: {} --> {}'
              .format(orderId, old[0][3], customerId))
        print('Change {} date: {} --> {}'
              .format(orderId, old[0][4], date))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def delete_connection():
        print('**************************************************************')
        print("PostgresSQL connection is closed")
        print('**************************************************************')

    @staticmethod
    def display_stored(name, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! You create new {} - {} to our {} list!'
              .format(tableName.lower(), name, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m')

    @staticmethod
    def display_many_stored(count, tableName):
        print('\033[92m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Hooray! You create {} new {} in {} table!'
              .format(tableName.lower(), count, tableName))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\033[0m')

    @staticmethod
    def display_deletion(anyId, tableName):
        print('\033[92m--------------------------------------------------------------')
        print('We have just removed {} with id:{} from table {}'
              .format(tableName.lower(), anyId, tableName))
        print(']--------------------------------------------------------------\033[0m')

    @staticmethod
    def show_list_items_orders(items, lastName):
        if items:
            print("--------------------ORDERS+ITEMS---------------------------------")
            print("|OrderId|", "CustomerId|", "ShopId|", "OrderDate  |", "ItemId   |", lastName)
            for row in items:
                print("|", row[0], "\t|", row[1], "\t\t|", row[2],
                      "\t|", row[3], "|", row[4], "\t\t|", row[5],
                      "\t\t\t|")
            print("-----------------------------------------------------------------")
        else:
            print("There is nothing with this id")

class Input(object):
    @staticmethod
    def input_id(tableName):
        inputId = input("Enter id {} ".format(tableName))
        return inputId

    @staticmethod
    def input_words():
        inputWord = input("Search item by word. Enter word or few word, if wou don't search touch 'Enter'\n ")
        if inputWord == '':
            return None
        return inputWord

    @staticmethod
    def input_two_value():
        inputFirst = input("Enter min value ")
        inputSecond = input("and max value ")
        return [inputFirst, inputSecond]

    @staticmethod
    def input_name():
        inputName = input("Enter name of item ")
        return inputName

    @staticmethod
    def input_count():
        inputCount = input("Enter count row more one ")
        return int(inputCount)

    @staticmethod
    def input_update_order(order):
        inputCount = input("if you want input your data enter - 0, otherwise there are default values \n")
        if inputCount == "0":
            inputItemId = input("Enter Item Id ")
            inputCustomerId = input("Enter Customer Id ")
            inputShopId = input("Enter Shop Id ")
            date = input("Enter date ")
            return {
                'itemId': inputItemId,
                'shopId': inputShopId,
                'customerId': inputCustomerId,
                'date': date
            }
        return order

    @staticmethod
    def input_update_item(item):
        inputCount = input("if you want input your data enter - 0, otherwise there are default values \n")
        if inputCount == "0":
            inputName = input("Enter Item Name ")
            inputPrice = input("Enter Item Price ")
            inputQuantity = input("Enter Quantity ")
            inputColor = input("Enter Item Color ")
            inputMaterial = input("Enter Material ")
            inputDescription = input("Enter description ")
            if inputDescription == "":
                inputDescription = None
            return {
                'name': inputName,
                'price': int(inputPrice),
                'quantity': int(inputQuantity),
                'color': inputColor,
                'material': inputMaterial,
                'description': inputDescription
            }
        return item

    @staticmethod
    def input_update_customer(customer):
        inputCount = input("if you want input your data enter - 0, otherwise there are default values \n")
        if inputCount == "0":
            inputName = input("Enter Customer Name ")
            inputPhone = input("Enter Customer Phone ")
            inputSex = input("Enter Customer Sex(female or male)")
            return {
                'name': inputName,
                'phone': inputPhone,
                'sex': inputSex
            }
        return customer

    @staticmethod
    def input_update_shop(shop):
        inputCount = input("if you want input your data enter - 0, otherwise there are default values \n")
        if inputCount == "0":
            inputName = input("Enter Shop Name ")
            inputStreet = input("Enter Shop Street ")
            return {
                'name': inputName,
                'street': inputStreet
            }
        return shop

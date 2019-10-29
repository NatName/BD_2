from BD_2.model import *
from BD_2.view import View
from BD_2.controller import *
from BD_2.menu import *


def main():
    item = ControllerItem(ModelItem, View)
    customer = ControllerCustomer(ModelCustomer, View)
    shop = ControllerShop(ModelShop, View)
    order = ControllerOrder(ModelOrder, View)

    menu(item, customer, shop, order)

    customer.disconnect()
    item.disconnect()
    order.disconnect()
    shop.disconnect()


if __name__ == '__main__':
    main()

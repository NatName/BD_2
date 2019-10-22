from BD_2.model import *
from BD_2.view import View
from BD_2.controller import *


def main():
    newShop = {
        'name': "name_10",
        'street': "street_10"
    }
    shop = ControllerShop(ModelShop, View)
    # shop.insert_many_shops(5)
    # shop.insert_shop(newShop)
    # shop.update_shop(13, newShop)
    shop.show_shop(12)
    # shop.delete_shop(12)
    shop.show_shops()
    shop.disconnect()
    newCustomer = {
        'name': "customer_10",
        'phone': "+380 68 568 93 45",
        'sex': 'female'
    }
    customer = ControllerCustomer(ModelCustomer, View)
    # customer.insert_many_customers(5)
    # customer.insert_customer(newCustomer)
    # customer.update_customer(67, newCustomer)
    # customer.delete_customer(4)
    customer.show_customers()
    customer.disconnect()

    item = ControllerItem(ModelItem, View)
    # item.insert_many_items(5)
    items = {
        'name': "item_5",
        'price': 2000,
        'quantity': 2,
        'color': "blue",
        'material': "steel"
    }
    # item.insert_item(items)
    # item.update_item(2, items)
    item.show_item(2)
    # item.delete_item(18)
    item.show_items()
    item.disconnect()

    newOrder = {
        'itemId': 29,
        'shopId': 1,
        'customerId': 1,
        'date': "2019-10-21"
    }

    order = ControllerOrder(ModelOrder, View)
    order.show_order_with_another_table(1, 30, "Item")
    # order.insert_many_orders(5)
    # order.insert_order(newOrder)
    order.show_order(6)
    # order.update_order(9, newOrder)
    # order.delete_order(11)
    order.show_orders()
    order.disconnect()


if __name__ == '__main__':
    main()

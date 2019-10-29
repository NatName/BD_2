from consolemenu import *
from consolemenu.items import *


def menu(item, customer, shop, order):
    newItem = {
        'name': "item_5",
        'price': 2000,
        'quantity': 2,
        'color': "blue",
        'material': "steel"
    }

    newCustomer = {
        'name': "customer_10",
        'phone': "+380 68 568 93 45",
        'sex': 'female'
    }

    newShop = {
        'name': "name_10",
        'street': "street_10"
    }

    newOrder = {
        'itemId': 35,
        'shopId': 1,
        'customerId': 1,
        'date': "2019-10-21"
    }

    # Create the menu
    mainMenu = ConsoleMenu("BD Shops")
    menu_items = ConsoleMenu("Item")
    menu_customer = ConsoleMenu("Customer")
    menu_shop = ConsoleMenu("Shop")
    menu_order = ConsoleMenu("Order")

    # A FunctionItem runs a Python function when selected
    function_show_item = FunctionItem("Show item", item.show_item, [])
    function_show_items = FunctionItem("Show items", item.show_items, [])
    function_insert_item = FunctionItem("Add one item", item.insert_item, [newItem])
    function_insert_many_items = FunctionItem("Add many items", item.insert_many_items, [])
    function_update_item = FunctionItem("Update one item", item.update_item, [newItem])
    function_delete_item = FunctionItem("Delete one items", item.delete_item, [])

    menu_items.append_item(function_show_item)
    menu_items.append_item(function_show_items)
    menu_items.append_item(function_insert_many_items)
    menu_items.append_item(function_insert_item)
    menu_items.append_item(function_update_item)
    menu_items.append_item(function_delete_item)

    function_show_customer = FunctionItem("Show customer", customer.show_customer, [])
    function_show_customers = FunctionItem("Show customers", customer.show_customers, [])
    function_insert_customer = FunctionItem("Add one customer", customer.insert_customer, [newCustomer])
    function_insert_many_customers = FunctionItem("Add many customers", customer.insert_many_customers, [])
    function_update_customer = FunctionItem("Update one customer", customer.update_customer, [newCustomer])
    function_delete_customer = FunctionItem("Delete one customers", customer.delete_customer, [])

    menu_customer.append_item(function_show_customer)
    menu_customer.append_item(function_show_customers)
    menu_customer.append_item(function_insert_customer)
    menu_customer.append_item(function_insert_many_customers)
    menu_customer.append_item(function_update_customer)
    menu_customer.append_item(function_delete_customer)

    function_show_shop = FunctionItem("Show shop", shop.show_shop, [])
    function_show_shops = FunctionItem("Show shops", shop.show_shops, [])
    function_insert_shop = FunctionItem("Add one shop", shop.insert_shop, [newShop])
    function_insert_many_shops = FunctionItem("Add many shops", shop.insert_many_shops, [])
    function_update_shop = FunctionItem("Update one shop", shop.update_shop, [newShop])
    function_delete_shop = FunctionItem("Delete one shops", shop.delete_shop, [])

    menu_shop.append_item(function_show_shop)
    menu_shop.append_item(function_show_shops)
    menu_shop.append_item(function_insert_shop)
    menu_shop.append_item(function_insert_many_shops)
    menu_shop.append_item(function_update_shop)
    menu_shop.append_item(function_delete_shop)

    function_show_order = FunctionItem("Show order", order.show_order, [])
    function_show_orders = FunctionItem("Show orders", order.show_orders, [])
    function_insert_order = FunctionItem("Add one order", order.insert_order, [newOrder])
    function_insert_many_orders = FunctionItem("Add many orders", order.insert_many_orders, [])
    function_update_order = FunctionItem("Update one order", order.update_order, [newOrder])
    function_delete_order = FunctionItem("Delete one orders", order.delete_order, [])
    function_show_order_by_quantity = FunctionItem("Show orders by ItemQuantity", order.show_order_by_quantity, [])
    function_show_order_by_item_name = FunctionItem("Show orders by ItemName", order.show_order_by_itemName, [])

    menu_order.append_item(function_show_order)
    menu_order.append_item(function_show_orders)
    menu_order.append_item(function_insert_order)
    menu_order.append_item(function_insert_many_orders)
    menu_order.append_item(function_update_order)
    menu_order.append_item(function_delete_order)
    menu_order.append_item(function_show_order_by_quantity)
    menu_order.append_item(function_show_order_by_item_name)

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_customer = SubmenuItem("Customers", menu_customer, mainMenu)
    submenu_item = SubmenuItem("Items", menu_items, mainMenu)
    submenu_shop = SubmenuItem("Shops", menu_shop, mainMenu)
    submenu_order = SubmenuItem("Orders", menu_order, mainMenu)

    # Once we're done creating them, we just add the items to the menu
    mainMenu.append_item(submenu_item)
    mainMenu.append_item(submenu_customer)
    mainMenu.append_item(submenu_shop)
    mainMenu.append_item(submenu_order)
    # Finally, we call show to show the menu and allow the user to interact
    mainMenu.show()

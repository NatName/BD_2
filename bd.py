from model import ModelShop
from view import View
from controller import ControllerShop


def main():
    print("1")
   # shop = ControllerShop(ModelShop, View)
    ControllerShop.insert_shop("name_4", "street_4")
    print("2")


if __name__ == '__main__':
    main()

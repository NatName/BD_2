from model import ModelShop
from view import View


class ControllerShop(object):

    def __init__(self):
        self.model = ModelShop
        self.view = View

    def insert_shop(self, name, street):
        print("3")
        self.model.create_shop(name, street)
        print("5")
        self.view.display_stored(name, "Shop")

from menu_items import Menu

class Food(Menu):
    def __init__(self, name, cost, description):
        super().__init__(name, cost)
        self._description = description
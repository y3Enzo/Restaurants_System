from .menu_items import Menu

class Drink(Menu):
    def __init__(self, name, cost, size):
        super().__init__(name, cost)
        self._size = size
        
    def __str__(self):
        return self._name
from .avaliation import Avaliation
from .menu.menu_items import Menu
from .menu.drink import Drink
from .menu.food import Food

class Restaurant:
    restaurants = list()
    def __init__(self, name: str, category: str):
        self._name = name.title().strip()
        self._category = category.title().strip()
        self._menu = list()
        self._avaliations = list()
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    @classmethod
    def list_restaurants(cls):
        print(f"\n{"Restaurant Name".ljust(20)} | {"Category".ljust(15)} | Avaliation")
        for restaurant in cls.restaurants:
            print(f"{restaurant._name.ljust(20)} | {restaurant._category.ljust(15)} | {restaurant.avaliations_average()}")

    def receive_avaliation(self, user: str, note: int):
        if not 0 <= note <= 5: return
        self._avaliations.append(Avaliation(user.strip().title(), note))

    def avaliations_average(self):
        sum = 0
        for avaliation in self._avaliations:
            sum += avaliation._note
        try:
            return round((sum / len(self._avaliations)), 1)
        except ZeroDivisionError:
            return "-"
            
    def add_in_menu(self, item):
        if isinstance(item, Menu):
            self._menu.append(item)

    def list_menu(self):
        print(f"\n{"Food".ljust(20)} | {"Cost".ljust(20)} | {"Description".ljust(20)}")
        for item in self._menu:
            if type(item) is Food:
                print(f"{item._name.ljust(20)} | {str(item._cost).ljust(20)} | {item._description.ljust(20)}")

        print(f"\n{"Drink".ljust(20)} | {"Cost".ljust(20)} | {"Size".ljust(20)}")
        for item in self._menu:
            if type(item) is Drink:
                print(f"{item._name.ljust(20)} | {str(item._cost).ljust(20)} | {item._size.ljust(20)}")
        
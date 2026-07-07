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
        self._status = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name} | {self._category}"

    def list_restaurants(self):
        if not self.restaurants:
            print("The restaurant list is empty")
            return

        print(f"\n{"Number".ljust(10)} | {"Restaurant Name".ljust(20)} | {"Category".ljust(15)} | {"Avaliation".ljust(15)} | Status")
        for number, restaurant in enumerate(self.restaurants, start=1):
            status = "Active" if restaurant._status else "Inactive"
            print(f"{str(number).ljust(10)} | {restaurant._name.ljust(20)} | {restaurant._category.ljust(15)} | {str(restaurant.avaliations_average()).ljust(15)} | {status}")

    def receive_avaliation(self, user: str, note: int):
        if not 0 <= note <= 5:
            print("The note isn't under 0 and 5")
            return False
        self._avaliations.append(Avaliation(user.strip().title(), note))
        return True

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
        if not self._menu:
            print("The restaurant menu is empty")
            return
        
        print(f"\n{"Number".ljust(10)} | {"Food".ljust(20)} | {"Cost".ljust(20)} | {"Description".ljust(20)}")
        for number, item in enumerate(self._menu, start=1):
            if type(item) is Food:
                print(f"{str(number).ljust(10)} | {item._name.ljust(20)} | {str(item._cost).ljust(20)} | {item._description.ljust(20)}")

        print(f"\n{"Number".ljust(10)} | {"Drink".ljust(20)} | {"Cost".ljust(20)} | {"Size".ljust(20)}")
        for number, item in enumerate(self._menu, start=1):
            if type(item) is Drink:
                print(f"{str(number).ljust(10)} | {item._name.ljust(20)} | {str(item._cost).ljust(20)} | {item._size.ljust(20)}")
        
    def change_status(self):
        self._status = not self._status

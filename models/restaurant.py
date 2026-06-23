from .avaliation import Avaliation

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
        print(f"{"Restaurant Name".ljust(20)} | {"Category".ljust(15)} | Avaliation")
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
            
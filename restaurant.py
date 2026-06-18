from avaliation import Avaliation

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

    @staticmethod
    def list_restaurants():
        print(f"{"Restaurant Name".ljust(20)} | {"Category".ljust(15)} | Avaliations")
        for restaurant in Restaurant.restaurants:
            print(f"{restaurant._name.ljust(20)} | {restaurant._category.ljust(15)} | {restaurant._avaliations}")

    def receive_avaliation(self, user: str, note: int):
        if not 0 <= note <= 5: return
        self._avaliations.append(Avaliation(user.strip().title(), note))

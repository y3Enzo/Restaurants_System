from models.restaurant import Restaurant
from models.menu.food import Food
from models.menu.drink import Drink

def create_restaurant():
    while True:
        print("\n")
        name = input("Restaurant name: ")
        if not name:
            print("ERROR: Restaurant name is empty")
            continue

        category = input("Category: ")
        if not category:
            print("ERROR: Restaurant category is empty")
            continue

        Restaurant(name, category)
        print(f"Restaurant {name}, category {category} created succesfully")
        break

def give_avaliation():
    while True:
        try:
            print("\n")
            restaurant = int(input("Restaurant number: "))
            restaurant -= 1
            user = input("Username: ")
            if not user:
                print("ERROR: The username is empty")
                continue
            note = int(input("Note: "))

            Restaurant.restaurants[restaurant].receive_avaliation(user, note)
            break
        except ValueError:
            print("ERROR: The value entered is not a number")
        except IndexError:
            print(f"ERROR: Don't exists a restaurant with number {restaurant + 1} in the list")


def add_in_menu():
    while True:
        try:
            print("\n")
            restaurant = int(input("Restaurant number: "))
            restaurant -= 1
            item = None

            print("[1] Food")
            print("[2] Drink")

            type = int(input("Select the item type by its number: "))
            name = input("Name: ")
            if not name:
                print("ERROR: The name is empty")
                continue

            cost = int(input("Cost: "))

            match type:
                case 1:
                    description = input("Description: ")
                    if not description:
                        print("ERROR: The item description is empty")
                        continue
                    item = Food(name, cost, description)
                case 2:
                    size = input("Size: ")
                    item = Drink(name, cost, size)
                case _:
                    print("ERROR: Invalid option")

            Restaurant.restaurants[restaurant].add_in_menu(item)
            break
        except ValueError:
            print("ERROR: The value entered is not a number")
        except IndexError:
            print(f"ERROR: Don't exists a restaurant with number {restaurant + 1} in the list")

def list_menu():
    while True:
        try:
            print("\n")
            restaurant = int(input("Restaurant number: "))
            restaurant -= 1
            Restaurant.restaurants[restaurant].list_menu()
            break
        except ValueError:
            print("ERROR: The value entered is not a number")
        except IndexError:
            print(f"ERROR: Don't exists a restaurant with number {restaurant + 1} in the list")

def main():
    while True:
        print("\n")
        print("""
┏┓┏┓┏┓  ┏┓
┃┃┃┃┃┃  ┃┃
┃┃┃┃┃┣━━┫┃┏━━┳━━┳┓┏┳━━┓
┃┃┃┃┃┃ ━┫┃┃┏━┫┏┓┃┗┛┃ ━┫
┃┗┛┗┛┃ ━┫┗┫┗━┫┗┛┃┃┃┃ ━┫
┗━━━━┻━━┻━┻━━┻━━┻┻┻┻━━┛""")
        print("[1] Create restaurant")
        print("[2] List restaurants")
        print("[3] Give avaliation")
        print("[4] Add item in restaurant menu")
        print("[5] List restaurant menu")
        print("[6] Exit")
        option = int(input("Select an option by its number: "))

        match option:
            case 1:
                create_restaurant()
            case 2:
                Restaurant.list_restaurants(Restaurant)
            case 3:
                give_avaliation()
            case 4:
                add_in_menu()
            case 5:
                list_menu()
            case 6:
                break
            case _:
                print("ERROR: Invalid option")

if __name__ == "__main__":
    main()

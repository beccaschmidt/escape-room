def show_menu(inventory):
    print()

    choices = [
        "Examine the desk",
        "Examine the portrait",
        "Examine the bookshelf",
        "Look at the door",
        "Check inventory",
        "Quit"
    ]

    if "brass key" in inventory:
        choices.insert(-1, "Open the desk drawer")

    for number, choice in enumerate(choices, start=1):
        print(f"{number}. {choice}")

def examine_desk(inventory):
    print("\nYou examine the desk.")
    print("There is a small locked drawer.")
    print("Beside it, you find a note.")
    print('The note reads: "The first number is hiding where time stands still."')

    if "brass key" not in inventory: 
        print("You also notice a small brass key underneath the desk.")
        inventory.append("brass key")
        print("You pick up the brass key.")

def examine_portrait():
    print("\nYou examine the portrait.")
    print("It shows an old man and a little girl smiling beside a grandfather clock. "
    "The glass on the clock is cracked and the time reads 7.15.")
    return True

def show_inventory(inventory): 
    print("\nInventory: ")

    if inventory: 
        for item in inventory:
            print(f"-{item}")
    else: 
        print("Your inventory is empty.")

def main():
    print("Welcome to the Escape Room!")

    name = input("What is your name? ").strip()

    print(f"Hello, {name}!")

    first_number_found = False
    inventory = []
    drawer_open = False

    while True:
        show_menu(inventory)

        choice = input("> ").strip()

        if choice == "1":
            examine_desk(inventory)
        elif choice == "2":
            first_number_found = examine_portrait()
        elif choice == "3":
            print("You examine the bookshelf.")
        elif choice == "4":
            print("You look at the door.")
        elif choice == "5":
            show_inventory(inventory)
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Please choose one of the available options.")


if __name__ == "__main__":
    main()
def italic(text):
    return f"\033[3m{text}\033[0m"


def yellow(text):
    return f"\033[33m{text}\033[0m"


def show_menu(inventory, drawer_open):
    print("\n" + "-" * 40)
    print("WHAT WOULD YOU LIKE TO DO?".center(40))
    print("-" * 40)

    choices = [
        "Examine the desk",
        "Examine the portrait",
        "Examine the bookshelf",
        "Look at the door",
        "Check inventory",
        "Quit"
    ]

    if "brass key" in inventory and not drawer_open:
        choices.insert(-1, "Open the desk drawer")

    for number, choice in enumerate(choices, start=1):
        print(yellow(f"{number}. {choice}"))

    return choices

def examine_desk(inventory):
    print("\n" + "-" * 40)
    print("THE DESK".center(40))
    print("-" * 40)

    print(italic("\nYou examine the desk."))
    print(italic("There is a small locked drawer."))
    print(italic("Beside it, you find a note."))
    print(italic('The note reads: "The first number is hiding where time stands still."'))

    if "brass key" not in inventory: 
        print(italic("You also notice a small brass key underneath the desk."))
        inventory.append("brass key")
        print(italic("You pick up the brass key."))

def open_drawer(inventory):
    print("\n" + "-" * 40)
    print("THE DESK DRAWER".center(40))
    print("-" * 40)

    print(italic("\nYou use the brass key to unlock the drawer."))
    print(italic("The drawer is stiff, but after some wiggling, it creaks and opens."))
    print(italic("Inside, you find a small piece of paper."))

    inventory.remove("brass key")
    return True

def examine_portrait():
    print("\n" + "-" * 40)
    print("THE PORTRAIT".center(40))
    print("-" * 40)

    print(italic("\nYou examine the portrait."))
    print(italic("It shows an old man and a little girl smiling beside a grandfather clock. "
                 "The glass on the clock is cracked and the time reads 7.15."))
    return True

def show_inventory(inventory): 
    print("\nInventory: ")

    if inventory: 
        for item in inventory:
            print(f"-{item}")
    else: 
        print("Your inventory is empty.")

def main():
    print("\n" + "-" * 40)
    print("WELCOME TO THE ESCAPE ROOM!".center(40))
    print("-" * 40)

    name = input("What is your name? ").strip()

    print(f"Hello, {name}!")

    first_number_found = False
    inventory = []
    drawer_open = False

    while True:
        choices = show_menu(inventory, drawer_open)

        choice = input("> ").strip()

        try:
            choice_index = int(choice) - 1
            choice = choices[choice_index]
        except ValueError:
            print("Please enter a number.")
            continue
        except IndexError:
            print("Please choose one of the available options.")
            continue

        if choice == "Examine the desk":
            examine_desk(inventory)
        elif choice == "Examine the portrait":
            first_number_found = examine_portrait()
        elif choice == "Examine the bookshelf":
            print("You examine the bookshelf.")
        elif choice == "Look at the door":
            print("You look at the door.")
        elif choice == "Check inventory":
            show_inventory(inventory)
        elif choice == "Open the desk drawer":
            drawer_open = open_drawer(inventory)
        elif choice == "Quit":
            print("Thanks for playing!")
            break
        else:
            print("Please choose one of the available options.")


if __name__ == "__main__":
    main()
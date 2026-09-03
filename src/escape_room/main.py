def italic(text):
    return f"\033[3m{text}\033[0m"


def yellow(text):
    return f"\033[33m{text}\033[0m"

def cyan(text):
    return f"\033[36m{text}\033[0m"

def underline(text):
    return f"\033[4m{text}\033[24m"


def show_menu(inventory, drawer_open):
    print("\n" + "-" * 40)
    print(yellow("WHAT WOULD YOU LIKE TO DO?".center(40)))
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

def examine_desk(inventory, note_found, drawer_open):
    print("\n" + "-" * 40)
    print(cyan("THE DESK".center(40)))
    print("-" * 40)

    print(cyan(italic("\nYou examine the desk.")))
    print(cyan(italic("It's neatly organised. A note sits in the middle.")))
    print(cyan(italic('The note reads: "The first number is hiding where time stands still."')))
    print()

    if "brass key" not in inventory and not drawer_open:
        print(cyan(italic("The desk has a small drawer which appears to be locked.\n")))
        print(cyan(italic("As you look around you notice a small brass key underneath the desk.")))
        inventory.append("brass key")
        print(cyan(italic("You pick up the brass key.")))

    if note_found:
        print(cyan(italic("\nThe piece of paper you found in the drawer is now resting on the desk.")))
        print(cyan(italic("'Two stand beside the clock.\n"
            "One tells you when.\n"
            "The other has a name worth remembering.'\n")))

def open_drawer(inventory):
    print("\n" + "-" * 40)
    print(cyan("THE DESK DRAWER".center(40)))
    print("-" * 40)

    print(cyan(italic("\nYou use the brass key to unlock the drawer.")))
    print(cyan(italic("The drawer is stiff, but after some wiggling, it creaks and opens.")))
    print(cyan(italic("Inside, you find a small piece of paper.")))
    print(cyan(italic("The paper reads:")))
    print()
    print(cyan(italic("'Two stand beside the clock.\n"
    "One tells you when.\n"
    "The other has a name worth remembering.'\n")))

    inventory.remove("brass key")
    return True, True

def examine_portrait():
    print("\n" + "-" * 40)
    print(cyan("THE PORTRAIT".center(40)))
    print("-" * 40)

    print(cyan(italic("\nYou examine the portrait.")))
    print()
    print(cyan(italic(
    "It shows a young man, who looks like your boss in younger years, with his arm around a smiling, little girl.\n"
    "Around her neck is a gold locket with the name 'Nina' engraved on it.\n"
    "The man is looking behind them at a grandfather clock.\n"
    "The glass on the clock is cracked and the time reads 7 o'clock.")))
    return True

def look_at_the_door():
    print("\n" + "-" * 40)
    print(cyan("THE DOOR".center(40)))
    print("-" * 40)

    print(cyan(italic("\nYou look at the door.\n"
                 "It looks old and rusty but the lock is secure.\n"
                 "There's a 4-digit keypad on the wall next to the door.")))

    code = input(yellow("Enter the 4-digit code: ")).strip()
    print()

    if code == "7982":
        print(cyan(italic("The keypad beeps. The lock clicks open.")))
        print(cyan(italic("You push the door open and quickly step out of the office.")))
        return True
    else:
        print(cyan(italic("The keypad beeps. The code is incorrect.")))

def show_inventory(inventory): 
    print("\nInventory: ")

    if inventory: 
        for item in inventory:
            print(f"-{item}")
    else: 
        print("Your inventory is empty.")

def examine_bookshelf():
    print("\n" + "-" * 40)
    print(cyan("THE BOOKSHELF".center(40)))
    print("-" * 40)

    print(cyan(italic("\nYou examine the bookshelf.")))
    print(cyan(italic(
    "Most of the books are covered in a thin layer of dust, "
    "but one is placed off to the side and looks noticeably more worn.")))
    print(cyan(italic(
    "You pull it from the shelf and notice a few small tags sticking out from the pages.")))
    print(cyan(italic(
    "The title catches your eye — a well-loved collection of children's poetry.")))
    print(cyan(italic(
    "You open the book and find that each tag marks the beginning of a different poem.")))
    print(cyan(italic(
    "You count eight tagged poems.")))
    print()
    print(cyan(italic(
    "As you return the book to the shelf, something catches your eye behind it.")))
    print(cyan(italic(
    "You reach behind the book and pull out a folded document.")))
    print(cyan(italic(
    "As you unfold it, you realise it's a death certificate.")))
    print()
    print(cyan(italic(
    "The name on the certificate makes you stop: Nina.")))
    print()
    print(cyan(italic(
    "Your eyes move to the date of death.")))
    print(cyan(italic(
    "You study the date carefully. The day of Nina's death was the 2nd.")))


def main():
    print("\n" + "-" * 40)
    print(yellow("WELCOME TO THE ESCAPE ROOM!".center(40)))
    print("-" * 40)

    name = input(yellow("What is your name? ")).strip()

    print(f"\nHello, {name}!")
    print(cyan(italic("\nYour snooping around seems to have put you in a pickle.\n"
                 "You were at your boss's dinner party at his old mansion\n"
                 "and upon entering what seemed to be his office the door slammed shut behind you.\n"
                 "The lock clicked and now the door won't budge.\n"
                 "You can very faintly still hear the noise of the party where your boss is giving a toast.")))

    first_number_found = False
    storybreak_triggered = False
    inventory = []
    drawer_open = False
    note_found = False

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
            examine_desk(inventory, note_found, drawer_open)
        elif choice == "Examine the portrait":
            if first_number_found and not storybreak_triggered:
                print(cyan(italic("\nA door slams somewhere in the mansion and pulls your focus away.")))
                print(cyan(italic("The walls shake slightly from the impact and the portrait shifts on the wall.")))
                storybreak_triggered = True
                print(cyan(italic("\nWhen you glance back at the portrait, you notice something carved into the edge of the frame.")))
                print(cyan(italic(f'"Where stories sleep, two final memories remain. '
                                f'{underline("FREE")} them by trailing favourite verses, '
                                f'{underline("BEFORE")} paying a final respect."')))
            else:
                first_number_found = examine_portrait()
        elif choice == "Examine the bookshelf":
            examine_bookshelf()
        elif choice == "Look at the door":
            escaped = look_at_the_door()
            if escaped:
                break
        elif choice == "Check inventory":
            show_inventory(inventory)
        elif choice == "Open the desk drawer":
            drawer_open, note_found = open_drawer(inventory)
        elif choice == "Quit":
            print("Thanks for playing!")
            break
        else:
            print("Please choose one of the available options.")


if __name__ == "__main__":
    main()
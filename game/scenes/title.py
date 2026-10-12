#title screen. also the main menu screen.

# game/scenes/title.py

import assets.art.game_title as game_title

def show_menu():
    game_title.aletheia()
    game_title.magic_wand()

    print("\nWelcome to Aletheia!") #change text later
    print("\na. Tutorial")
    print("b. Start game")
    print("c. Customize your mahou shoujo")
    print("d. Quit")

    while True:
        choice = input("> ").strip().lower()

        if choice == "a":
            print("Starting tutorial...")
            break
        elif choice == "b":
            print("Starting game...")
            break
        elif choice == "c":
            print("Opening customization...")
            break
        elif choice == "d":
            print("Goodbye!")
            break
        else:
            print(
                "Invalid choice! Please enter a, b, c, or d. "
                "Unless you want to be cursed. ψ(｀∇´)ψ"
            )

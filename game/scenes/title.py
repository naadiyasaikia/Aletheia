#title screen. also the main menu screen.
import assets.art.game_title as game_title
print("this is a test")
game_title.aletheia()
game_title.magic_wand()

print("Welcome to Aletheia, a text-based magical girl fight game.") #this text is to be replaced oml cringe


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
        print("Invalid choice! please enter a, b, c, or d - unless you want to be cursed. ψ(｀∇´)ψ")


from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines, draw_box
from game.assets import load_art
from game.data.characters import CHARACTERS, PETS
from game.data.skills import SKILLS
from game.state import state
from game.scenes.gacha import GachaScene


class CustomizeScene(Scene):
    def __init__(self):
        super().__init__()
        self.time = 0

        # Calculate maximum art size for the box
        self.art_h = 0
        self.art_w = 0

        for c in CHARACTERS:
            art = load_art("girls", c["art"])

            if len(art) > self.art_h:
                self.art_h = len(art)

            for line in art:
                if len(line) > self.art_w:
                    self.art_w = len(line)

        self.box_x = 2
        self.box_y = 2
        self.box_w = self.art_w + 6
        self.box_h = self.art_h + 4
        self.text_x = self.box_x + self.box_w + 3

    def update(self, dt):
        self.time = self.time + dt

    def handle_input(self, key):
        # Return to the previous scene
        if key == 27:
            self.engine.pop_scene()

        # Open the pet gacha
        elif key in (ord("g"), ord("G")):
            self.engine.push_scene(GachaScene())

        # Equip the next unlocked pet
        elif key in (ord("p"), ord("P")):
            owned_indices = [
                i for i, pet in enumerate(PETS)
                if pet in state.owned_pets
            ]

            if owned_indices:
                current = state.pet

                try:
                    position = owned_indices.index(current)
                    position = (position + 1) % len(owned_indices)
                except ValueError:
                    position = 0

                state.pet = owned_indices[position]

        # Choose a character
        else:
            for i in range(len(CHARACTERS)):
                if key == ord("a") + i:
                    state.character = i

    def draw(self, stdscr):
        char = CHARACTERS[state.character]
        tx = self.text_x

        # Draw the character box and art
        draw_box(
            stdscr,
            self.box_y,
            self.box_x,
            self.box_h,
            self.box_w
        )

        # Animate the character's gentle bobbing
        bob = 0
        if int(self.time * 2) % 2 == 1:
            bob = 1

        draw_lines(
            stdscr,
            self.box_y + 1 + bob,
            self.box_x + 3,
            load_art("girls", char["art"])
        )

        # Character selection
        draw_text(stdscr, 2, tx, "CHARACTER")

        for i in range(len(CHARACTERS)):
            letter = chr(ord("a") + i)
            mark = ">" if i == state.character else " "

            draw_text(
                stdscr,
                3 + i,
                tx,
                mark + " " + letter + ". " + CHARACTERS[i]["name"]
            )

        # Character stats
        draw_text(stdscr, 8, tx, "Name: " + char["name"])
        draw_text(stdscr, 9, tx, "HP:   " + str(char["hp"]))

        # Character skills
        draw_text(stdscr, 11, tx, "Skills:")

        for i in range(len(char["skills"])):
            skill = SKILLS[char["skills"][i]]

            draw_text(
                stdscr,
                12 + i,
                tx + 2,
                str(i + 1) + ". " + skill["name"]
                + " (" + str(skill["cooldown"]) + "s)"
            )

        # Equipped pet and gacha menu
        draw_text(
            stdscr,
            17,
            tx,
            "Pet: " + PETS[state.pet] + "  [p] equip"
        )

        draw_text(stdscr, 18, tx, "[g] Gacha")

        # Controls
        draw_text(
            stdscr,
            21,
            3,
            "a/b/c: choose  p: equip pet  g: gacha  ESC: back"
        )

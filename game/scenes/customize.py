from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines, draw_box
from game.assets import load_art
from game.data.characters import CHARACTERS, PETS
from game.data.skills import SKILLS
from game.state import state


class CustomizeScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.time = 0

        # calculate max art size for box generate
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
        if key == 27:
            self.engine.pop_scene()
        elif key == ord("p"):
            state.pet = (state.pet + 1) % len(PETS)
        else:
            for i in range(len(CHARACTERS)):
                if key == ord("a") + i:
                    state.character = i

    def draw(self, stdscr):
        char = CHARACTERS[state.character]
        tx = self.text_x

        # box and character art
        draw_box(stdscr, self.box_y, self.box_x, self.box_h, self.box_w)
        bob = 0
        if int(self.time * 2) % 2 == 1:
            bob = 1
        draw_lines(stdscr, self.box_y + 1 + bob, self.box_x + 3, load_art("girls", char["art"]))

        # stats and skills
        draw_text(stdscr, 2, tx, "CHARACTER")
        for i in range(len(CHARACTERS)):
            letter = chr(ord("a") + i)
            mark = ">" if i == state.character else " "
            draw_text(stdscr, 3 + i, tx, mark + " " + letter + ". " + CHARACTERS[i]["name"])

        draw_text(stdscr, 8, tx, "Name: " + char["name"])
        draw_text(stdscr, 9, tx, "HP:   " + str(char["hp"]))

        draw_text(stdscr, 11, tx, "Skills:")
        for i in range(len(char["skills"])):
            skill = SKILLS[char["skills"][i]]
            draw_text(stdscr, 12 + i, tx + 2, str(i + 1) + ". " + skill["name"] + " (" + str(skill["cooldown"]) + "s)")

        draw_text(stdscr, 17, tx, "Pet: " + PETS[state.pet] + "  [p] change")
        draw_text(stdscr, 21, 3, "a/b/c: choose   p: pet   ESC: back")

import random

from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines, draw_box
from game.assets import load_frames
from game.data.characters import PETS
from game.state import state


class GachaScene(Scene):

    def __init__(self):
        super().__init__()

        self.rolling = False
        self.timer = 0.0
        self.frame_duration = 0.4

        self.frames = load_frames("fx", "wishEgg")

        self.result = None
        self.message = "Press R to roll the gacha!"
        self.roll_cost = 200
        self.top_up_amount = 500
        self.pending_pet = None

    def update(self, dt):
        if not self.rolling:
            return

        self.timer += dt

        # Finish after displaying every frame
        if self.timer >= self.frame_duration * len(self.frames):
            self.rolling = False
            self.result = self.pending_pet

            if self.result not in state.owned_pets:
                state.owned_pets.append(self.result)
                self.message = "NEW PET UNLOCKED!"
            else:
                self.message = "You already own this pet!"

    def buy_crystals(self):
        if self.rolling:
            return
        state.soul_crystals += self.top_up_amount
        self.message = f"You bought {self.top_up_amount} soul crystals!" #demo for hackathon, not real implementation of a shop system
    def start_roll(self):
        if self.rolling:
            return

        if state.soul_crystals < self.roll_cost:
            self.message = f"Not enough soul crystals! (Need {self.roll_cost})."
            return

        state.soul_crystals -= self.roll_cost
        # Exclude "None": it is not a gacha reward
        self.pending_pet = random.choice(PETS[1:])

        self.rolling = True
        self.timer = 0.0
        self.result = None
        self.message = "Your wish is being granted..."

    def handle_input(self, key):
        if key == 27:  # ESC
            self.engine.pop_scene()

        elif key in (ord("r"), ord("R")):
            self.start_roll()

        elif key in (ord("b"), ord("B")):
            self.buy_crystals()

    def draw(self, stdscr):

        draw_text(stdscr, 4, 5, "Soul Crystals: " + str(state.soul_crystals))
        draw_box(stdscr, 2, 2, 26, 55)

        draw_text(stdscr, 3, 5, "PET GACHA")
        draw_text(stdscr, 5, 5, self.message)

        if self.rolling:
            # Select the current animation frame
            index = int(self.timer / self.frame_duration)
            index = min(index, len(self.frames) - 1)

            draw_lines(stdscr, 7, 8, self.frames[index])

        elif self.result is not None:
            draw_text(stdscr, 8, 5, "You obtained:")
            draw_text(stdscr, 10, 7, self.result)

        else:
            draw_text(stdscr, 8, 5, "       .-''''-.")
            draw_text(stdscr, 9, 5, "      /  WISH  \\")
            draw_text(stdscr, 10, 5, "      \\   EGG  /")
            draw_text(stdscr, 11, 5, "       '-.__.-'")

        draw_text(stdscr, 21, 5, "[R] Roll - 200 Soul Crystals")
        draw_text(stdscr, 23, 5, "[B] Buy +500 Soul Crystals (DEMO)")
        draw_text(stdscr, 25, 5, "[ESC] Return to customization")
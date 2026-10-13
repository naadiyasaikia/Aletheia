from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines
from game.assets import load_art

class TitleScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.phase = "logo"          # phase 1 logo -> phase 2 menu
        self.timer = 0
        self.message = ""
        self.logo = load_art("logo")
        self.wand = load_art("wand")

    def update(self, dt):
        # t3 seconds showing logo
        if self.phase == "logo":
            self.timer = self.timer + dt
            if self.timer >= 3:
                self.phase = "menu"

    def handle_input(self, key):
        # if logo phase, any key will go to menu
        if self.phase == "logo":
            self.phase = "menu"
            return

        if key == ord("a"):
            self.message = "Tutorial: not yet implemented"
        elif key == ord("b"):
            from game.scenes.battle import BattleScene
            self.engine.push_scene(BattleScene())
        elif key == ord("c"):
            self.message = "Customize: not yet implemented"
        elif key == ord("d"):
            self.engine.pop_scene()
        else:
            self.message = "Invalid choice! Please enter a, b, c, or d. " "Unless you want to be cursed. ψ(｀∇´)ψ"
    def draw(self, stdscr):
        if self.phase == "logo":
            draw_lines(stdscr, 6, 0, self.logo)
            draw_text(stdscr, 19, 28, "Press any key...")
        else:
            draw_lines(stdscr, 1, 2, self.wand)          # wand on left
            draw_text(stdscr, 6, 90, "Welcome to Aletheia!")
            draw_text(stdscr, 9, 90, "a. Tutorial")
            draw_text(stdscr, 10, 90, "b. Start game")
            draw_text(stdscr, 11, 90, "c. Customize")
            draw_text(stdscr, 12, 90, "d. Quit")
            draw_text(stdscr, 15, 90, self.message)
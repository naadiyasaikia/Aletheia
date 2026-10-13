from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines
from game.assets import load_art
from game.scenes.cutscene import CutsceneScene
from game.data.story import INTRO

class TitleScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.phase = "logo"
        self.timer = 0
        self.message = ""
        self.logo = load_art("logo")
        self.wand = load_art("wand")
        self.awaiting_intro_finish = False

    def start_intro(self):
        if self.phase == "intro":
            return
        self.phase = "intro"
        self.awaiting_intro_finish = True
        self.engine.push_scene(CutsceneScene(INTRO))

    def update(self, dt):
        if self.phase == "logo":
            self.timer = self.timer + dt
            if self.timer >= 3:
                self.start_intro()
        elif self.phase == "intro":
            if self.awaiting_intro_finish and self.engine.stack[-1] is self:
                self.phase = "menu"
                self.awaiting_intro_finish = False

    def handle_input(self, key):
        if self.phase == "logo":
            self.start_intro()
            return

        if self.phase == "intro":
            return

        if key == ord("a"):
            self.message = "Tutorial: not yet implemented"
        elif key == ord("b"):
            from game.scenes.battle import BattleScene
            self.engine.push_scene(BattleScene())
        elif key == ord("c"):
            from game.scenes.customize import CustomizeScene
            self.engine.push_scene(CustomizeScene())
        elif key == ord("d"):
            self.engine.pop_scene()
        else:
            text = "Invalid choice! You want to be cursed? ψ(｀∇´)ψ"
            self.message = text
    def draw(self, stdscr):
        if self.phase == "logo":
            draw_lines(stdscr, 6, 0, self.logo)
            draw_text(stdscr, 19, 70, "Press any key...")
        else:
            draw_lines(stdscr, 1, 2, self.wand)
            draw_text(stdscr, 6, 90, "Welcome to Aletheia!")
            draw_text(stdscr, 9, 90, "a. Tutorial")
            draw_text(stdscr, 10, 90, "b. Start game")
            draw_text(stdscr, 11, 90, "c. Customize")
            draw_text(stdscr, 12, 90, "d. Quit")
            draw_text(stdscr, 15, 90, self.message)
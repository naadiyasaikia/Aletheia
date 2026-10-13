from pathlib import Path

from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines


class TutorialScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        tutorial_path = Path(__file__).resolve().parents[2] / "assets" / "tutorial.txt"
        raw = tutorial_path.read_text(encoding="utf-8")
        self.pages = [page.split("\n") for page in raw.split("\n=====\n")]
        self.index = 0

    def handle_input(self, key):
        if key == 27:
            self.engine.pop_scene()
        elif key == 10 or key == 13 or key == ord(" "):
            self.index = self.index + 1
            if self.index >= len(self.pages):
                self.engine.pop_scene()      # empty -> title

    def draw(self, stdscr):
        draw_lines(stdscr, 2, 2, self.pages[self.index])
        draw_text(stdscr, 21, 3, "[Enter] next page    [ESC] back")
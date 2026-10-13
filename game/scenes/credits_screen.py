from pathlib import Path

from game.scenes.base import Scene
from game.renderer import draw_box, draw_text


class CreditsScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        credits_path = Path(__file__).resolve().parents[2] / "assets" / "credits.txt"
        self.lines = credits_path.read_text(encoding="utf-8").splitlines()

    def handle_input(self, key):
        if key == 27 or key in (10, 13, 32):
            self.engine.pop_scene()

    def draw(self, stdscr):
        draw_box(stdscr, 2, 2, 20, 120)
        draw_text(stdscr, 3, 5, " Aletheia Credits ")
        for i, line in enumerate(self.lines):
            draw_text(stdscr, 5 + i, 6, line)
        draw_text(stdscr, 18, 6, "[Esc/Enter/Space] Back")
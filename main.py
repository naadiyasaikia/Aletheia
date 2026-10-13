import curses
from game.engine import Engine
from game.scenes.base import Scene
from game import config
from game.scenes.battle import BattleScene

# test scene
class DummyScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.x = 10
        self.y = 5

    def handle_input(self, key):
        if key == ord("q"):
            self.engine.pop_scene()
        elif key == curses.KEY_LEFT:
            self.x = self.x - 1
        elif key == curses.KEY_RIGHT:
            self.x = self.x + 1
        elif key == curses.KEY_UP:
            self.y = self.y - 1
        elif key == curses.KEY_DOWN:
            self.y = self.y + 1

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, "@")


#========MAIN FLOW OF THE GAME========
def main(stdscr):
    engine = Engine(stdscr)
    engine.push_scene(BattleScene())
    engine.run()


if __name__ == "__main__":
    curses.wrapper(main)
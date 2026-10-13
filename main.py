import curses
from game.engine import Engine
from game.scenes.base import Scene
from game import config
from game.scenes.title import TitleScene
from game.scenes.battle import BattleScene

#========MAIN FLOW OF THE GAME========
def main(stdscr):
    engine = Engine(stdscr)
    engine.push_scene(TitleScene())
    engine.run()


if __name__ == "__main__":
    curses.wrapper(main) 
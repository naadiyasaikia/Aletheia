#template to inherit from for all scenes
class Scene:
    def __init__(self):
        self.engine = None

    def handle_input(self, key):
        pass

    def update(self, dt):       #dt: delta time (time between 2 frames, in a second)
        pass

    def draw(self, stdscr):     #standard screen: the curses window to draw on
        pass
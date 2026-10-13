from game.scenes.base import Scene
from game.renderer import draw_text, draw_box


class CutsceneScene(Scene):
    def __init__(self, script, next_scene=None):
        Scene.__init__(self)
        self.script = script
        self.next_scene = next_scene   # next scene
        self.index = 0                 # index in lines list
        self.time = 0                  # time
        self.speed = 40                # text speed

    def current_text(self):
        return self.script[self.index][1]

    def visible_text(self):
        count = int(self.time * self.speed)
        return self.current_text()[:count]

    def is_done(self):
        return len(self.visible_text()) >= len(self.current_text())

    def update(self, dt):
        self.time = self.time + dt

    def handle_input(self, key):
        if key == 27:
            self.finish()                       # ESC: skip cutscene
        elif key == 10 or key == 13 or key == ord(" "):
            if not self.is_done():
                self.time = 9999                
            else:
                self.index = self.index + 1     # next line
                self.time = 0
                if self.index >= len(self.script):
                    self.finish()

    def finish(self):
        if self.next_scene != None:
            self.engine.change_scene(self.next_scene())
        else:
            self.engine.pop_scene()

    def draw(self, stdscr):
        who = self.script[self.index][0]
        draw_box(stdscr, 15, 2, 7, 140)
        if who != "":
            draw_text(stdscr, 15, 5, " " + who + " ")
        draw_text(stdscr, 17, 5, self.visible_text())
        if self.is_done():
            draw_text(stdscr, 20, 130, "[Enter] >")
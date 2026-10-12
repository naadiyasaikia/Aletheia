import time
import curses
from game import config

class Engine:
    def __init__(self, standard_screen):
        self.standard_screen = standard_screen
        self.stack = []     #STACK MANAGEMENT: stack of scenes
        curses.curs_set(0)      #hide the cursor
        standard_screen.nodelay(True)    #don't wait for user input
        standard_screen.keypad(True)      #enable special keys (like arrows)

    #==============STACK METHODS================
    #use engine to push and pop scenes, so that the current scene can be changed
    def push_scene(self, scene):
        scene.engine = self
        self.stack.append(scene)

    def pop_scene(self):
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            raise Exception("Scene stack is empty, cannot pop scene.")

    def change_scene(self, scene):
        self.pop_scene()
        self.push_scene(scene)

    # replace the current scene with a new one
    def change_scene(self, scene):
        self.pop_scene()
        self.push_scene(scene)

    #=================MAIN LOOP================
    def run(self):
        frame_time = 1 / config.FPS
        last = time.time()

        while len(self.stack) > 0:
            #calculate delta time
            start = time.time()
            delta_time = start - last
            last = start

            #handle input
            key = self.standard_screen.getch()
            if key != -1:
                self.stack[-1].handle_input(key)
            if len(self.stack) == 0:
                break

            # update the current scene
            self.stack[-1].update(delta_time)

            if len(self.stack) == 0:
                break

            # erase -> draw -> refresh the current scene
            self.standard_screen.erase()
            self.stack[-1].draw(self.standard_screen)
            self.standard_screen.refresh()

            # limit the frame rate
            used = time.time() - start
            if used < frame_time:
                time.sleep(frame_time - used)
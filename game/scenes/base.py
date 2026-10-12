#template to inherit from for all scenes
class Scene:
    def __init__(self):
        self.engine = None

    def handle_input(self, key):
        pass

    def update(self, delta_time):       #time between 2 frames, in a second
        pass

    def draw(self, standard_screen):
        pass
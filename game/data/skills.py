class Skill:
    def __init__(self, data):
        self.name = data["name"]
        self.cooldown = data["cooldown"]
        self.cd_left = 0

    def update(self, dt):
        if self.cd_left > 0:
            self.cd_left = self.cd_left - dt
            if self.cd_left < 0:
                self.cd_left = 0

    def ready(self):
        return self.cd_left == 0

    def use(self):
        self.cd_left = self.cooldown
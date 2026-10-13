class Skill:
    def __init__(self, data):
        self.name = data["name"]
        self.cooldown = data["cooldown"]     # seconds
        self.damage = data.get("damage", 0)
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

    def ratio(self):
        #to draw the cooldown bar later
        return self.cd_left / self.cooldown

class Skill:
    def __init__(self, data):
        self.name = data["name"]
        self.cooldown = data["cooldown"]
        self.damage = data.get("damage", 0)
        self.heal = data.get("heal", 0)
        self.charges = data.get("charges", -1)    # -1 = unlimited
        self.cd_left = 0
        if data.get("starts_charging"):           # ultimate: starts charging at the beginning of the battle
            self.cd_left = self.cooldown

    def update(self, dt):
        if self.cd_left > 0:
            self.cd_left = self.cd_left - dt
            if self.cd_left < 0:
                self.cd_left = 0

    def ready(self):
        if self.charges == 0:                     # ultimate: no charges left
            return False
        return self.cd_left == 0

    def use(self):
        self.cd_left = self.cooldown
        if self.charges > 0:
            self.charges = self.charges - 1

    def ratio(self):
        return self.cd_left / self.cooldown
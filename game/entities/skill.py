class Skill:
    def __init__(self, data):
        self.name = data["name"]
        self.cooldown = data["cooldown"]
        self.damage = data.get("damage", 0)
        self.heal = data.get("heal", 0)
        self.charges = data.get("charges", -1)    # -no litmit
        self.fx = data.get("fx", "fx_hit")
        self.cast = data.get("cast", 0.2)
        self.fx_at = data.get("fx_at", "enemies")
        self.cd_left = 0
        if data.get("starts_charging"):
            self.cd_left = self.cooldown

    def update(self, dt):
        if self.cd_left > 0:
            self.cd_left = self.cd_left - dt
            if self.cd_left < 0:
                self.cd_left = 0

    def ready(self):
        if self.charges == 0:
            return False
        return self.cd_left == 0

    def use(self):
        self.cd_left = self.cooldown
        if self.charges > 0:
            self.charges = self.charges - 1

    def ratio(self):
        return self.cd_left / self.cooldown
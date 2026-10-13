class Enemy:
    def __init__(self, data):
        self.name = data["name"]
        self.hp = data["hp"]
        self.max_hp = data["hp"]
        self.damage = data["damage"]
        self.attack_cd = data["attack_cd"]
        self.timer = 0

    def update(self, dt):
        # update the attack timer and return damage if the enemy can attack
        self.timer = self.timer + dt
        if self.timer >= self.attack_cd:
            self.timer = 0
            return self.damage
        return 0

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

    def is_dead(self):
        return self.hp <= 0
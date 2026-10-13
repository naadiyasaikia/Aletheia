import random
from game.scenes.base import Scene
from game.renderer import draw_text
from game.entities.skill import Skill
from game.entities.enemy import Enemy
from game.data.skills import SKILLS
from game.data.enemies import ENEMIES
from game.battle.skill_effect import EFFECTS


class BattleScene(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.player_max_hp = 100
        self.player_hp = 100
        self.shield_time = 0

        # skills list from state (update this with custom skills later)
        self.skill_ids = ["star_burst", "moon_shield", "heart_beam"]

        self.basic = Skill(SKILLS["basic"])
        self.skills = []
        for sid in self.skill_ids:
            self.skills.append(Skill(SKILLS[sid]))

        self.enemies = []
        self.spawn_timer = 0

    def use_skill(self, skill, effect_name):
        if skill.ready():
            used = EFFECTS[effect_name](self, skill)
            if used:
                skill.use()

    def handle_input(self, key):
        if key == 27:
            self.engine.pop_scene()
        elif key == ord("1"):
            self.use_skill(self.basic, "basic")
        elif key == ord("2"):
            self.use_skill(self.skills[0], self.skill_ids[0])
        elif key == ord("3"):
            self.use_skill(self.skills[1], self.skill_ids[1])
        elif key == ord("4"):
            self.use_skill(self.skills[2], self.skill_ids[2])

    def update(self, dt):
        # cooldown
        self.basic.update(dt)
        for s in self.skills:
            s.update(dt)

        # shield time
        if self.shield_time > 0:
            self.shield_time = self.shield_time - dt

        # spawn
        self.spawn_timer = self.spawn_timer + dt
        if self.spawn_timer >= 2.0 and len(self.enemies) < 5:
            self.spawn_timer = 0
            key = random.choice(list(ENEMIES))
            self.enemies.append(Enemy(ENEMIES[key]))

        # player get hit by enemies
        for e in self.enemies:
            dmg = e.update(dt)
            if self.shield_time <= 0:
                self.player_hp = self.player_hp - dmg

        # enemy die
        alive = []
        for e in self.enemies:
            if not e.is_dead():
                alive.append(e)
        self.enemies = alive

        # lose condition
        if self.player_hp <= 0:
            self.engine.pop_scene()

    #cooldown bar text
    def cd_bar(self, skill):
        full = int((1 - skill.ratio()) * 10)
        return "█" * full + "░" * (10 - full)

    def draw(self, stdscr):
        # HP
        draw_text(stdscr, 1, 2, "HP: " + str(self.player_hp) + "/" + str(self.player_max_hp))
        if self.shield_time > 0:
            draw_text(stdscr, 2, 2, "SHIELD " + str(round(self.shield_time, 1)) + "s")

        # char on left
        draw_text(stdscr, 10, 8, "\\(^o^)/")

        # enemy list on right
        for i in range(len(self.enemies)):
            e = self.enemies[i]
            draw_text(stdscr, 3 + i * 3, 50, "<" + e.name + "> " + str(e.hp) + "/" + str(e.max_hp))

        # skill bar on bottom
        draw_text(stdscr, 21, 2, "[1] " + self.basic.name + " " + self.cd_bar(self.basic))
        for i in range(len(self.skills)):
            s = self.skills[i]
            text = "[" + str(i + 2) + "] " + s.name + " " + self.cd_bar(s)
            draw_text(stdscr, 22, 2 + i * 26, text)
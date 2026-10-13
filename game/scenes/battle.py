import random
from game.scenes.base import Scene
from game.renderer import draw_text, draw_lines
from game.entities.skill import Skill
from game.entities.enemy import Enemy
from game.data.skills import SKILLS
from game.data.enemies import ENEMIES
from game.data.characters import CHARACTERS
from game.battle.skill_effects import EFFECTS
from game.state import state
from game.assets import load_art, load_frames

class BattleScene(Scene):
    def __init__(self, round_number=1):
        Scene.__init__(self)
        self.round_number = round_number
        if round_number == 1:
            self.kills_to_win = 5
        elif round_number == 2:
            self.kills_to_win = 10
        else:
            self.kills_to_win = 10

        char = CHARACTERS[state.character]
        self.player_max_hp = char["hp"]
        self.player_hp = char["hp"]
        self.player_art = load_art("girls", char["art"])
        self.casting = None
        #for skill position
        self.fx_positions = {
            "player":  (6, 2),
            "enemies": (4, 38),
            "center":  (2, 20),
        }
        # 4 skills, each skill has its own cooldown and charges
        self.skill_ids = char["skills"]
        self.skills = []
        for sid in self.skill_ids:
            self.skills.append(Skill(SKILLS[sid]))

        # shield time
        self.shield_time = 0     # no damage for 2 seconds
        self.block_time = 0      # block next hit for 3 seconds
        self.veil_time = 0       # reduce damage by 70% for 1.5 seconds

        self.enemies = []
        self.spawn_timer = 0
        self.kills = 0

    def evaluate_round_result(self):
        if self.kills >= self.kills_to_win:
            from game.scenes.title import TitleScene

            if self.round_number == 1:
                from game.data.story import WIN_ROUND
                from game.scenes.cutscene import CutsceneScene
                self.engine.change_scene(CutsceneScene(WIN_ROUND, next_scene=lambda: BattleScene(round_number=2)))
                return

            if self.round_number == 2:
                from game.data.story import GAME_OVER
                from game.scenes.cutscene import CutsceneScene
                self.engine.change_scene(CutsceneScene(GAME_OVER, next_scene=lambda: TitleScene()))
                return

        if self.player_hp <= 0:
            from game.data.story import LOSE_ROUND
            from game.scenes.cutscene import CutsceneScene
            from game.scenes.title import TitleScene
            self.engine.change_scene(CutsceneScene(LOSE_ROUND, next_scene=lambda: TitleScene()))

    def take_hit(self, dmg):
        if self.shield_time > 0:
            return
        if self.block_time > 0:
            self.block_time = 0          # block only 1 hit
            return
        if self.veil_time > 0:
            dmg = int(dmg * 0.3)         # reduce damage by 70%
        self.player_hp = self.player_hp - dmg

    def handle_input(self, key):
        if key == 27:
            self.engine.pop_scene()
        elif key == ord("1"):
            self.use_skill(0)
        elif key == ord("2"):
            self.use_skill(1)
        elif key == ord("3"):
            self.use_skill(2)
        elif key == ord("4"):
            self.use_skill(3)

    def update(self, dt):
        if self.casting != None:
            self.casting["timer"] = self.casting["timer"] + dt
            skill = self.skills[self.casting["index"]]
            if self.casting["timer"] >= skill.cast:
                self.finish_cast()
        for s in self.skills:
            s.update(dt)

        if self.shield_time > 0:
            self.shield_time = self.shield_time - dt
        if self.block_time > 0:
            self.block_time = self.block_time - dt
        if self.veil_time > 0:
            self.veil_time = self.veil_time - dt

        # spawn
        self.spawn_timer = self.spawn_timer + dt
        if self.spawn_timer >= 2.0 and len(self.enemies) < 5:
            self.spawn_timer = 0
            key = random.choice(list(ENEMIES))
            self.enemies.append(Enemy(ENEMIES[key]))

        # enemy hit player
        for e in self.enemies:
            dmg = e.update(dt)
            if dmg > 0:
                self.take_hit(dmg)

        # enemy die -> remove from list
        alive = []
        for e in self.enemies:
            if not e.is_dead():
                alive.append(e)
            else:
                self.kills = self.kills + 1
        self.enemies = alive

        self.evaluate_round_result()

    def cd_bar(self, skill):
        if skill.charges == 0:
            return "░" * 10 + " EMPTY"
        full = int((1 - skill.ratio()) * 10)
        bar = "█" * full + "░" * (10 - full)
        if skill.ready():
            if skill.charges > 0:
                return bar + " READY x" + str(skill.charges)
            return bar + " READY"
        return bar + " " + str(round(skill.cd_left, 1)) + "s"

    def draw(self, stdscr):
        draw_text(stdscr, 1, 2, "HP: " + str(self.player_hp) + "/" + str(self.player_max_hp))
        if self.shield_time > 0:
            draw_text(stdscr, 2, 2, "INVULNERABLE " + str(round(self.shield_time, 1)) + "s")
        if self.block_time > 0:
            draw_text(stdscr, 3, 2, "MIST: blocks next hit")
        if self.veil_time > 0:
            draw_text(stdscr, 4, 2, "VEIL: -70% damage")

        # character on the left
        draw_lines(stdscr, 7, 4, self.player_art)

        #skill animation
        self.draw_fx(stdscr)

        # enemy on the right, each enemy takes 3 lines
        for i in range(len(self.enemies)):
            e = self.enemies[i]
            y = 1 + i * 4
            draw_lines(stdscr, y, 52, load_art("enemies", e.art))
            draw_text(stdscr, y + 3, 52, e.name + " " + str(e.hp) + "/" + str(e.max_hp))


        # 4 skill, each line: [1] Skill Name  █████░░░░░  2.3s
        for i in range(len(self.skills)):
            s = self.skills[i]
            draw_text(stdscr, 19 + i, 2, "[" + str(i + 1) + "] " + s.name + "  " + self.cd_bar(s))

    #==========Skill Animation============
    def use_skill(self, index):
        if self.casting != None:
            return
        skill = self.skills[index]
        if skill.ready():
            self.casting = {"index": index, "timer": 0.0}

    def finish_cast(self):
        index = self.casting["index"]
        self.casting = None
        skill = self.skills[index]
        used = EFFECTS[self.skill_ids[index]](self, skill)   # damage/heal
        if used:
            skill.use()                                      # cooldown

    def draw_fx(self, stdscr):
        if self.casting == None:
            return
        skill = self.skills[self.casting["index"]]
        try:
            frames = load_frames("fx", skill.fx)
        except FileNotFoundError:
            frames = load_frames("fx", "fx_hit")

        n = int(self.casting["timer"] / skill.cast * len(frames))
        if n >= len(frames):
            n = len(frames) - 1

        y, x = self.fx_positions[skill.fx_at]
        draw_lines(stdscr, y, x, frames[n])
        draw_text(stdscr, 1, 30, skill.name + "!")
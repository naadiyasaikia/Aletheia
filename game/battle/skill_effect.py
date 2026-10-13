import random

# each function get (scene, skill).
# true if the skill is used successfully, false if not (like no target) 

def basic_attack(scene, skill):
    if len(scene.enemies) == 0:
        return False
    target = random.choice(scene.enemies)
    target.take_damage(skill.damage)
    return True


def star_burst(scene, skill):
    # hit ALL enemies
    if len(scene.enemies) == 0:
        return False
    for e in scene.enemies:
        e.take_damage(skill.damage)
    return True


def heart_beam(scene, skill):
    # hit most Hp enemy
    if len(scene.enemies) == 0:
        return False
    target = scene.enemies[0]
    for e in scene.enemies:
        if e.hp > target.hp:
            target = e
    target.take_damage(skill.damage)
    return True


def moon_shield(scene, skill):
    # 3s shield
    scene.shield_time = 3.0
    return True


def heal(scene, skill):
    scene.player_hp = scene.player_hp + 25
    if scene.player_hp > scene.player_max_hp:
        scene.player_hp = scene.player_max_hp
    return True


# table for skills
EFFECTS = {
    "basic": basic_attack,
    "star_burst": star_burst,
    "heart_beam": heart_beam,
    "moon_shield": moon_shield,
    "heal": heal,
}
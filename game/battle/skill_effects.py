import random

# each skill effect function takes in the scene and the skill object
# returns True if the skill was used successfully, False otherwise


def add_hp(scene, amount):
    scene.player_hp = scene.player_hp + amount
    if scene.player_hp > scene.player_max_hp:
        scene.player_hp = scene.player_max_hp


# ---------- random hit (Petal Burst, Cloudburst, Starshot, Thorn Shower)
def single_hit(scene, skill):
    if len(scene.enemies) == 0:
        return False
    target = random.choice(scene.enemies)
    target.take_damage(skill.damage)
    return True


# ---------- hit and reset timer (Thunderclap)
def thunderclap(scene, skill):
    if len(scene.enemies) == 0:
        return False
    target = random.choice(scene.enemies)
    target.take_damage(skill.damage)
    target.timer = 0
    return True


# ---------- hit 3 enemies in a row (Starfall)
def starfall(scene, skill):
    if len(scene.enemies) == 0:
        return False
    i = random.randrange(len(scene.enemies))
    for j in range(i - 1, i + 2):
        if 0 <= j < len(scene.enemies):
            scene.enemies[j].take_damage(skill.damage)
    return True


# ---------- Fruit Heal
def fruit_heal(scene, skill):
    add_hp(scene, skill.heal)
    return True


# ---------- Garden of Rebirth: 70 dmg to the enemy with the most HP and 70 heal to the player
def garden_of_rebirth(scene, skill):
    if len(scene.enemies) == 0:
        return False
    target = scene.enemies[0]
    for e in scene.enemies:
        if e.hp > target.hp:
            target = e
    target.take_damage(skill.damage)
    add_hp(scene, skill.heal)
    return True


# ---------- Mist Drift: block all damage for 3 seconds
def mist_drift(scene, skill):
    scene.block_time = 3.0
    return True


# ---------- Lunar Veil: reduce all damage for 1.5 seconds
def lunar_veil(scene, skill):
    scene.veil_time = 1.5
    return True


# ---------- Tempest Waltz: 5 hits x 14 = 70, invincible for 2 seconds
def tempest_waltz(scene, skill):
    if len(scene.enemies) == 0:
        return False
    per_hit = skill.damage // 5
    for i in range(5):
        if len(scene.enemies) > 0:
            target = random.choice(scene.enemies)
            target.take_damage(per_hit)
    scene.shield_time = 2.0
    return True


# ---------- Supernova: 70 damage to all enemies
def supernova(scene, skill):
    if len(scene.enemies) == 0:
        return False
    for e in scene.enemies:
        e.take_damage(skill.damage)
    return True


EFFECTS = {
    "petal_burst": single_hit,
    "thorn_shower": single_hit,
    "fruit_heal": fruit_heal,
    "garden_of_rebirth": garden_of_rebirth,

    "cloudburst": single_hit,
    "thunderclap": thunderclap,
    "mist_drift": mist_drift,
    "tempest_waltz": tempest_waltz,

    "starshot": single_hit,
    "starfall": starfall,
    "lunar_veil": lunar_veil,
    "supernova": supernova,
}
# fx    = file name
# cast  = animation duration
# fx_at = location

SKILLS = {
    # --- Flowergirl ---
    "petal_burst":       {"name": "Petal Burst",       "cooldown": 0.6,  "damage": 15,
                          "fx": "fx_hit", "cast": 0.2, "fx_at": "enemies"},
    "thorn_shower":      {"name": "Thorn Shower",      "cooldown": 2.5,  "damage": 25,
                          "fx": "fx_thorn_shower", "cast": 0.5, "fx_at": "center"},
    "fruit_heal":        {"name": "Fruit Heal",        "cooldown": 1.0,  "heal": 40, "charges": 2,
                          "fx": "fx_fruit_heal", "cast": 0.6, "fx_at": "player"},
    "garden_of_rebirth": {"name": "Garden of Rebirth", "cooldown": 30.0, "damage": 70, "heal": 70,
                          "starts_charging": True,
                          "fx": "fx_garden_of_rebirth", "cast": 1.0, "fx_at": "center"},

    # --- Cloudygirl ---
    "cloudburst":        {"name": "Cloudburst",        "cooldown": 0.6,  "damage": 15,
                          "fx": "fx_hit", "cast": 0.2, "fx_at": "enemies"},
    "thunderclap":       {"name": "Thunderclap",       "cooldown": 2.5,  "damage": 25,
                          "fx": "fx_big", "cast": 0.4, "fx_at": "enemies"},
    "mist_drift":        {"name": "Mist Drift",        "cooldown": 6.0,
                          "fx": "fx_shield", "cast": 0.3, "fx_at": "player"},
    "tempest_waltz":     {"name": "Tempest Waltz",     "cooldown": 30.0, "damage": 70,
                          "starts_charging": True,
                          "fx": "fx_garden_of_rebirth", "cast": 1.0, "fx_at": "center"},

    # --- Starlightgirl ---
    "starshot":          {"name": "Starshot",          "cooldown": 0.6,  "damage": 15,
                          "fx": "fx_hit", "cast": 0.2, "fx_at": "enemies"},
    "starfall":          {"name": "Starfall",          "cooldown": 2.5,  "damage": 30,
                          "fx": "fx_big", "cast": 0.4, "fx_at": "enemies"},
    "lunar_veil":        {"name": "Lunar Veil",        "cooldown": 7.0,
                          "fx": "fx_shield", "cast": 0.3, "fx_at": "player"},
    "supernova":         {"name": "Supernova",         "cooldown": 30.0, "damage": 70,
                          "starts_charging": True,
                          "fx": "fx_garden_of_rebirth", "cast": 1.0, "fx_at": "center"},
}
from pathlib import Path

ART_DIR = Path(__file__).parent.parent / "assets" / "art"
_cache = {}


def load_art(name):
    if name not in _cache:
        text = (ART_DIR / (name + ".txt")).read_text(encoding="utf-8")
        _cache[name] = text.rstrip("\n").split("\n")
    return _cache[name]
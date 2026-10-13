from pathlib import Path

ART_DIR = Path(__file__).parent.parent / "assets" / "art"
_cache = {}
_frame_cache = {}


def _resolve_art_path(folder, name=None):
    if name is None:
        name = folder
        folder = ""

    if folder:
        return ART_DIR / folder / (name + ".txt")
    return ART_DIR / (name + ".txt")


def _read(folder, name=None):
    path = _resolve_art_path(folder, name)
    return path.read_text(encoding="utf-8").rstrip("\n")


def load_art(folder, name=None):
    # return list
    if name is None:
        name = folder
        folder = ""

    key = (folder + "/" if folder else "") + name
    if key not in _cache:
        _cache[key] = _read(folder, name).split("\n")
    return _cache[key]


def load_frames(folder, name=None):
    # frame is being separated by =====
    if name is None:
        name = folder
        folder = ""

    key = (folder + "/" if folder else "") + name
    if key not in _frame_cache:
        frames = []
        for part in _read(folder, name).split("\n=====\n"):
            frames.append(part.split("\n"))
        _frame_cache[key] = frames
    return _frame_cache[key]
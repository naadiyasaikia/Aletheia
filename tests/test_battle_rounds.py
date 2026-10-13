import unittest

from game.data.story import GAME_OVER, WIN_ROUND
from game.scenes.battle import BattleScene
from game.scenes.cutscene import CutsceneScene


class DummyEngine:
    def __init__(self):
        self.scene = None

    def change_scene(self, scene):
        self.scene = scene


class BattleRoundTests(unittest.TestCase):
    def test_round_targets(self):
        self.assertEqual(BattleScene(round_number=1).kills_to_win, 5)
        self.assertEqual(BattleScene(round_number=2).kills_to_win, 10)

    def test_round_flow(self):
        engine = DummyEngine()

        round1 = BattleScene(round_number=1)
        round1.engine = engine
        round1.kills = round1.kills_to_win
        round1.evaluate_round_result()
        self.assertIsInstance(engine.scene, CutsceneScene)
        self.assertEqual(engine.scene.script, WIN_ROUND)

        engine = DummyEngine()
        round2 = BattleScene(round_number=2)
        round2.engine = engine
        round2.kills = round2.kills_to_win
        round2.evaluate_round_result()
        self.assertIsInstance(engine.scene, CutsceneScene)
        self.assertEqual(engine.scene.script, GAME_OVER)


if __name__ == "__main__":
    unittest.main()

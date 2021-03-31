import unittest
import sys
from pathlib import Path
sys.path.append(str(Path('__file__').resolve().parent))
from source.variations import *
from source.json import to_json


class TestVariations(unittest.TestCase):
    """test class of variations.py
    """
    design = VariationDesign(SystemImageLabel("azooKey"))
    press_actions = [
        ToggleCapsLockStateAction(),
        MoveCursorAction(-4),
        MoveTabAction(TabType.custom, "flick_greek")
    ]
    start = [
        InputAction("¡™£"),
        ReplaceLastCharactersAction(
            {"クレヨンしんちゃん": "ドラえもん", "妖怪ウォッチ": "ポケモン"}),
    ]
    repeat = [
        EnableResizingModeAction(),
        SmartDeleteDefaultAction(),
    ]

    def test_Variation(self):
        """test method for Variation
        """
        longpress_actions = LongpressAction(self.start, self.repeat)
        variation = Variation(
            self.design, self.press_actions, longpress_actions)
        expected_json = {
            "design": to_json(self.design),
            "press_actions": to_json(self.press_actions),
            "longpress_actions": to_json(longpress_actions),
        }
        self.assertEqual(expected_json, to_json(variation))

    def test_FlickDirection(self):
        """test method for FlickDirection
        """
        actual = json.dumps(FlickDirection.left)
        self.assertEqual("\"left\"", actual)

        actual = json.dumps(FlickDirection.top)
        self.assertEqual("\"top\"", actual)

        actual = json.dumps(FlickDirection.bottom)
        self.assertEqual("\"bottom\"", actual)

        actual = json.dumps(FlickDirection.right)
        self.assertEqual("\"right\"", actual)

    def test_FlickVariationData(self):
        """test method for FlickVariationData
        """
        longpress_actions = LongpressAction(self.start, self.repeat)
        variation = Variation(
            self.design, self.press_actions, longpress_actions)
        data = FlickVariationData(FlickDirection.bottom, variation)
        expected_json = {
            "type": "flick_variation",
            "direction": FlickDirection.bottom,
            "key": to_json(variation)
        }
        self.assertEqual(expected_json, to_json(data))

    def test_LongpressVariationData(self):
        """test method for LongpressVariationData
        """
        longpress_actions = LongpressAction(self.start, self.repeat)
        variation = Variation(
            self.design, self.press_actions, longpress_actions)
        data = LongpressVariationData(variation)
        expected_json = {
            "type": "longpress_variation",
            "key": to_json(variation)
        }
        self.assertEqual(expected_json, to_json(data))


if __name__ == "__main__":
    unittest.main()

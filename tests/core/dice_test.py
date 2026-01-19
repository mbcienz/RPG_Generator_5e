import unittest
from core.constant import MIN_DICE_VALUE, MAX_DICE_FACES
from core.exceptions import DiceFacesTypeError, DiceFacesValueError
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_constructor1(self): 
        dice = Dice()
        self.assertEqual(dice.get_faces(), 20)

    def test_constructor2(self):
        dice = Dice(10)
        self.assertEqual(dice.get_faces(), 10)

    def test_constructor3(self):
        with self.assertRaises(DiceFacesValueError):
            Dice(-1)

    def test_constructor4(self):
        with self.assertRaises(DiceFacesValueError):
            Dice(30)

    def test_constructor5(self):
        with self.assertRaises(DiceFacesTypeError):
            Dice(10.5)

    def test_constructor6(self):
        with self.assertRaises(DiceFacesTypeError):
            Dice("hello")

    def test_generate_value(self):
        dice = Dice()
        result = dice.roll()
        self.assertLessEqual(result, MAX_DICE_FACES)
        self.assertGreaterEqual(result, MIN_DICE_VALUE)

    def set_faces1(self):
        FACES = 10
        dice = Dice()
        dice.set_faces(FACES)
        self.assertEqual(dice.get_faces(), FACES)
    
    def set_faces2(self):
        FACES = -10
        dice = Dice()
        with self.assertRaises(DiceFacesValueError):
            dice.set_faces(FACES)

    def set_faces3(self):
        FACES =8.2
        dice = Dice()
        with self.assertRaises(DiceFacesTypeError):
            dice.set_faces(FACES)

    def set_faces4(self):
        FACES = "hello"
        dice = Dice()
        with self.assertRaises(DiceFacesTypeError):
            dice.set_faces(FACES)

    def test_get_faces(self):
        dice = Dice()
        self.assertEqual(MAX_DICE_FACES, dice.get_faces())

    def test_roll(self):
        dice = Dice()
        result = dice.roll()
        self.assertLessEqual(result, MAX_DICE_FACES)
        self.assertGreaterEqual(result, MIN_DICE_VALUE)


if __name__ == "__main__":
    unittest.main()
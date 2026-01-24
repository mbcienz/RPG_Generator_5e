import unittest
from core.constant import MIN_DICE_VALUE, MAX_DICE_FACES
from core.exceptions import DiceFacesTypeError, DiceFacesValueError
from core.dice import Dice

class TestDice(unittest.TestCase):

    def test_constructor1(self):
        """Create the dice and check the default number of faces.
        """ 
        dice = Dice()
        self.assertEqual(dice.get_faces(), 20)

    def test_constructor2(self):
        """Create the dice with 10 faces.
        """
        dice = Dice(10)
        self.assertEqual(dice.get_faces(), 10)

    def test_constructor3(self):
        """Create a dice with an invalid value number of faces. Negative number.
        """
        with self.assertRaises(DiceFacesValueError):
            Dice(-1)

    def test_constructor4(self):
        """Create a dice with an invalid value number of faces. Value higher than the default max number of faces.
        """
        with self.assertRaises(DiceFacesValueError):
            Dice(30)

    def test_constructor5(self):
        """Create a dice with an invalid type of number of faces. Float value.
        """
        with self.assertRaises(DiceFacesTypeError):
            Dice(10.5)

    def test_constructor6(self):
        """Create a dice with an invalid type of number of faces. String value.
        """
        with self.assertRaises(DiceFacesTypeError):
            Dice("hello")

    def test_generate_value(self):
        """Create a dice and check if the generated number is between min possible value and the number of faces.
        """
        dice = Dice()
        result = dice.roll()
        self.assertLessEqual(result, MAX_DICE_FACES)
        self.assertGreaterEqual(result, MIN_DICE_VALUE)

    def test_set_faces1(self):
        """Create a dice and set the number of faces to 10.
        """
        FACES = 10
        dice = Dice()
        dice.set_faces(FACES)
        self.assertEqual(dice.get_faces(), FACES)
    
    def test_set_faces2(self):
        """Create a dice and set the number of faces to and invalid value.
        """
        FACES = -10
        dice = Dice()
        with self.assertRaises(DiceFacesValueError):
            dice.set_faces(FACES)

    def test_set_faces3(self):
        """Create a dice and set the number of faces to and invalid type.
        """
        FACES =8.2
        dice = Dice()
        with self.assertRaises(DiceFacesTypeError):
            dice.set_faces(FACES)

    def test_set_faces4(self):
        """Create a dice and set the number of faces to and invalid type.
        """
        FACES = "hello"
        dice = Dice()
        with self.assertRaises(DiceFacesTypeError):
            dice.set_faces(FACES)

    def test_get_faces(self):
        """Create a dice and get the actual number of faces.
        """
        dice = Dice()
        self.assertEqual(MAX_DICE_FACES, dice.get_faces())

    def test_roll(self):
        """Create a dice and check if the generated number is between min possible value and the number of faces.
        """
        dice = Dice()
        result = dice.roll()
        self.assertLessEqual(result, MAX_DICE_FACES)
        self.assertGreaterEqual(result, MIN_DICE_VALUE)


if __name__ == "__main__":
    unittest.main()
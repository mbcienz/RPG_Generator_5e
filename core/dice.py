from core.constant import DEFAULT_DICE_FACES, MAX_DICE_FACES, MIN_DICE_VALUE
from core.exceptions import DiceFacesValueError, DiceFacesTypeError
import random

class Dice:
    def __init__(self, faces=DEFAULT_DICE_FACES):
        self._check_faces_value(faces)
        self.faces = faces


    #### PRIVATE METHODS ####
    def _check_faces_value(self, faces): 
        """Check first if faces is an integer. If it is not, then raise a DiceFacesTypeError exception, otherwise check if the value is between min and max value. If it is not, then raise a DiceFacesValueError exception. 

        Args:
            faces (int): number of faces for the dice. It must be a value between the MIN_DICE_VALUE and MAX_DICE_FACES constants

        Raises:
            DiceFacesTypeError: Exception that defines the type of the faces argument
            DiceFacesValueError: Exception that defines the value of the faces argument
        """
        if not isinstance(faces, int): 
            raise DiceFacesTypeError()
        if faces > MAX_DICE_FACES or faces < MIN_DICE_VALUE:
            raise DiceFacesValueError()
        


    def _generate_value(self):
        """Generate a random value between a min value and the actual number of faces.

        Returns:
            int: the generated number.
        """
        return random.randint(MIN_DICE_VALUE, self.faces)


    #### PUBLIC METHODS ####
    def set_faces(self, faces):
        """Set the number of faces for the dice.

        Args:
            faces (int): number of faces for the dice. It must be a value between the MIN_DICE_VALUE and MAX_DICE_FACES constants
        """
        self._check_faces_value(faces)
        self.faces = faces


    def get_faces(self):
        """Return the current number of faces.

        Returns:
            int: the value stored in the attribute faces.
        """
        return self.faces


    def roll(self):
        """Generate a random value between a min value and the actual number of faces.

        Returns:
            int: the generated number.
        """
        return self._generate_value()
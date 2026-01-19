from core.constant import DEFAULT_DICE_FACES, MAX_DICE_FACES, MIN_DICE_VALUE
from core.exceptions import DiceFacesValueError, DiceFacesTypeError
import random

class Dice:
    def __init__(self, faces=DEFAULT_DICE_FACES):
        self._check_faces_value(faces)
        self.faces = faces


    #### PRIVATE METHODS ####
    def _check_faces_value(self, faces): 
        # check first if faces is an integer. If it is not, then raise a DiceFacesTypeError exception,
        # otherwise check if the value is between min and max value. If it is not, then raise a 
        # DiceFacesValueError exception. 
        if not isinstance(faces, int): 
            raise DiceFacesTypeError()
        if faces > MAX_DICE_FACES or faces < MIN_DICE_VALUE:
            raise DiceFacesValueError()
        


    def _generate_value(self):
        # generate a random value between a min value and the actual number of faces
        return random.randint(MIN_DICE_VALUE, self.faces)


    #### PUBLIC METHODS ####
    def set_faces(self, faces):
        self._check_faces_value(faces)
        self.faces = faces


    def get_faces(self):
        return self.faces


    def roll(self):
        return self._generate_value()
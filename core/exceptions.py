class DiceFacesValueError(Exception):
    "Raised when the user want to define a dice with an invalid number of faces"
    pass

class DiceFacesTypeError(Exception):
    "Raised when the user want to define a dice with an invalid type of faces"
    pass
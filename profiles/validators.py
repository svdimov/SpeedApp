from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ProfileUserValidator:
    def __init__(self, message=None)->None:
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Username must contain only letters, digits, and underscores!"
        else:
            self.__message = value

    def __call__(self, value:str, *args, **kwargs)->None:
        for char in value:
            if not(char.isalnum() or char == '_'):
                raise ValidationError(self.message)





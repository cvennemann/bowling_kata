import abc


class Rollgenerator(abc.ABC):
    @abc.abstractmethod
    def get_next_roll(self):
        pass


class StringToRollGenerator(Rollgenerator):
    def __init__(self, string_of_rolls: str):
        self.__string_of_rolls = self.__validate_string(string_of_rolls)
        self.__rolls_as_int = self.__string_to_int()

    @staticmethod
    def __validate_string(string_of_rolls):
        if type(string_of_rolls) != str:
            raise TypeError()

        for char in string_of_rolls:
            if char not in '123456789/-X ':
                raise ValueError(f"Unexpected character: {char}")

        return string_of_rolls

    def __string_to_int(self):
        rolls_as_int = []
        for char in self.__string_of_rolls:
            int_char = None
            if char == ' ':
                continue
            elif char.isdecimal():
                int_char = int(char)
            elif char == 'X':
                int_char = 10
            elif char == '-':
                int_char = 0
            elif char == '/':
                int_char = 10 - rolls_as_int[-1]

            rolls_as_int.append(int_char)

        return rolls_as_int

    def get_next_roll(self):
        for number in self.__rolls_as_int:
            yield number

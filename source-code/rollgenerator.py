import abc


class RollGenerator(abc.ABC):
    """
    A RollGenerator implements the method .get_next_roll() to return integers that represent
    the amount of pins knocked over by a bowling ball.
    """
    @abc.abstractmethod
    def get_next_roll(self):
        pass


class StringToRollGenerator(RollGenerator):
    """
    StringToRollGenerator takes a string of valid bowling notation turns it into a list of integers.
    .get_next_roll() accesses a generator object that yields the integers one at a time.
    """
    def __init__(self, string_of_rolls: str):
        self.__string_of_rolls = self.__validate_string_of_rolls(string_of_rolls)
        self.__rolls_as_int = self.__string_to_list_of_ints()
        self.__roll_generator = self.__make_roll_generator()

    @staticmethod
    def __validate_string_of_rolls(string_of_rolls: str) -> str:
        # Raises an Error if the argument is not a string or contains an invalid character.
        if type(string_of_rolls) != str:
            raise TypeError('Expected type: string')

        for char in string_of_rolls:
            if char not in '123456789/X-F ':
                raise ValueError(f"Unexpected character: {char}")

        return string_of_rolls

    def __string_to_list_of_ints(self) -> [int]:
        rolls_as_int = []
        for char in self.__string_of_rolls:
            int_char = None
            if char == ' ':
                continue
            elif char.isdecimal():
                int_char = int(char)
            elif char == 'X':
                int_char = 10
            elif char == '-' or char == 'F':
                int_char = 0
            elif char == '/':
                int_char = 10 - rolls_as_int[-1]

            rolls_as_int.append(int_char)

        return rolls_as_int

    def __make_roll_generator(self):
        # Generator function from a list of integers.
        for number in self.__rolls_as_int:
            yield number

    def get_next_roll(self) -> int:
        # Returns the next value of the generator function.
        return next(self.__roll_generator)

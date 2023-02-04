import abc


class Rollgenerator(abc.ABC):
    @abc.abstractmethod
    def get_next_roll(self):
        pass


class StringToRollGenerator:
    def __init__(self, list_of_rolls: [int]):
        self.__list_of_rolls = []

    def get_next_roll(self):
        for roll in [-1, -1, -1, -1, -1]:
            yield roll

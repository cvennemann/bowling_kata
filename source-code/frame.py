import abc


class Frame(abc.ABC):
    def receive_a_roll(self, num_pins: int) -> bool:
        pass

    @abc.abstractmethod
    def get_base_score(self):
        pass

    @abc.abstractmethod
    def get_bonus_rolls_score(self):
        pass

    @abc.abstractmethod
    def get_total_score(self):
        pass


class RegularFrame(Frame):
    def get_base_score(self) -> int:
        return -1

    def get_bonus_rolls_score(self) -> int:
        return -1

    def get_total_score(self) -> int:
        return -1


class LastFrame(Frame):
    def get_base_score(self) -> int:
        return -1

    def get_bonus_rolls_score(self) -> int:
        return -1

    def get_total_score(self) -> int:
        return -1

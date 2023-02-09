import abc


class Frame(abc.ABC):
    """
    A Frame receives individual rolls and counts them according to the bowling rules.
    If a Frame has received fewer regular rolls than expected, rolls will be appended to self._regular_rolls.
    Else, if a Frame has received fewer bonus rolls than expected, rolls will be appended to self._bonus_rolls.
    A Frame can return its regular score, bonus score and total score.
    """
    def __init__(self):
        self._standing_pins: int = 10
        self._expected_frame_rolls: int = 2
        self._expected_bonus_rolls: int = 0
        self._regular_rolls: list = []
        self._bonus_rolls: list = []

    @property
    def regular_rolls(self):
        return self._regular_rolls

    def regular_rolls_are_full(self) -> bool:
        return len(self._regular_rolls) == self._expected_frame_rolls

    def bonus_rolls_are_full(self) -> bool:
        return len(self._bonus_rolls) == self._expected_bonus_rolls

    def is_full(self) -> bool:
        return self.regular_rolls_are_full() and self.bonus_rolls_are_full()

    def receive_a_roll(self, roll: int):
        self._append_roll(roll)
        self._standing_pins -= roll
        self._adjust_expectations_on_spare_strike(roll)

    def _append_roll(self, roll: int):
        if not self.regular_rolls_are_full():
            self._regular_rolls.append(roll)

        elif not self.bonus_rolls_are_full():
            self._bonus_rolls.append(roll)

    def get_regular_score(self) -> int:
        return sum(self._regular_rolls)

    def get_bonus_score(self) -> int:
        return sum(self._bonus_rolls)

    def get_total_score(self) -> int:
        if self.is_full():
            return self.get_regular_score() + self.get_bonus_score()

    @abc.abstractmethod
    def _adjust_expectations_on_spare_strike(self, roll: int):
        pass


class RegularFrame(Frame):
    """
    Frame one through nine in a regular bowling game.
    Inherits from Frame and implements the method ._adjust_expectations_on_spare_strike().
    """
    def _adjust_expectations_on_spare_strike(self, roll: int):
        if self._standing_pins:
            return

        if self._regular_rolls == [10]:
            self._expected_frame_rolls = 1
            self._expected_bonus_rolls = 2
        else:
            self._expected_bonus_rolls = 1


class LastFrame(Frame):
    """
    The tenth and last Frame in a regular bowling game.
    Inherits from Frame and implements the method ._adjust_expectations_on_spare_strike().
    """
    def _adjust_expectations_on_spare_strike(self, roll: int):
        if self._standing_pins:
            return

        if self._regular_rolls == [10]:
            self._expected_frame_rolls = 3
            self._standing_pins = 10

        elif sum(self._regular_rolls[0:2]) == 10:
            self._expected_frame_rolls = 3
            self._standing_pins = 10

import abc


class Frame(abc.ABC):
    def __init__(self):
        self._standing_pins = 10
        self._expected_frame_rolls = 2
        self._expected_bonus_rolls = 0
        self._frame_rolls = []
        self._bonus_rolls = []

    def frame_is_full(self):
        return len(self._frame_rolls) == self._expected_frame_rolls

    def bonus_is_full(self):
        return len(self._bonus_rolls) == self._expected_bonus_rolls

    def is_full(self):
        return self.frame_is_full() and self.bonus_is_full()

    def receive_a_roll(self, roll: int):
        self._append_roll(roll)
        self._standing_pins -= roll
        self._adjust_spare_strike(roll)
        print('frame rolls:', self._frame_rolls, self.frame_is_full(), self._expected_frame_rolls)
        print('bonus rolls:', self._bonus_rolls, self.bonus_is_full(), self._expected_bonus_rolls)

    def _append_roll(self, roll):
        if not self.frame_is_full():
            self._frame_rolls.append(roll)

        elif not self.bonus_is_full():
            self._bonus_rolls.append(roll)

    @abc.abstractmethod
    def _adjust_spare_strike(self, roll):
        pass

    def get_base_score(self) -> int:
        return sum(self._frame_rolls)

    def get_bonus_score(self) -> int:
        return sum(self._bonus_rolls)

    def get_total_score(self) -> int:
        return self.get_base_score() + self.get_bonus_score()


class RegularFrame(Frame):
    def _adjust_spare_strike(self, roll):
        if self._standing_pins:
            return

        if self._frame_rolls == [10]:
            self._expected_frame_rolls = 1
            self._expected_bonus_rolls = 2
        else:
            self._expected_bonus_rolls = 1


class LastFrame(Frame):
    def _adjust_spare_strike(self, roll):
        if self._standing_pins:
            return

        if self._frame_rolls[0] == 10:
            self._expected_frame_rolls = 3
            self._expected_bonus_rolls = 0
            self._standing_pins = 10

        elif sum(self._frame_rolls[0:2]) == 10:
            self._expected_frame_rolls = 3
            self._standing_pins = 10

import abc
import os
import time


class ScoreOutput(abc.ABC):
    """
    The generate_output() method receives a list of tuples. Each tuple represent the rolls of one Frame and
    the total score of the Frame if the frame is already completed, else None:
        [
            ( [roll1, roll2], score1 ),  <- frame 1
            ( [roll3, roll4], score2 ),  <- frame 2
            ( [roll5], None ),           <- frame 3
            ( [roll6], None)             <- frame 4
        ]
    """

    def __init__(self):
        self._frame_rolls = None

    @abc.abstractmethod
    def generate_output(self, input_data: tuple):
        pass


class TerminalOutput(ScoreOutput):
    """
    TerminalOutput Prints the results of a complete or incomplete bowling game to console in a neat little ASCII table.

    If the TerminalOutput in instantiated with a valid argument for the time.sleep() function,
    the program will pause for that long after the output has been printed to console.
    """
    def __init__(self, pause_seconds=0):
        super().__init__()
        self.__pause_seconds = pause_seconds

        self.__print_empty_table()

    def __print_empty_table(self):
        self.__clear()
        print("+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+")
        print("|   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |     10    |")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+")
        print("|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |")
        print("|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---+---+")
        print("|       |       |       |       |       |       |       |       |       |           |")
        print("+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+")

    @staticmethod
    def __clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def generate_output(self, input_data: tuple):
        self._frame_rolls = input_data

        self.__clear()
        print("+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+")
        print("|   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |     10    |")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+")

        roll_value_string = self.__draw_roll_values()
        print(roll_value_string)

        print("|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---|   +---+---+")

        score_string = self.__draw_score()
        print(score_string)

        print("+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+")

        time.sleep(self.__pause_seconds)

    def __draw_roll_values(self) -> str:
        roll_value_string = ''

        for frame_idx in range(9):
            roll1, roll2 = self.__get_roll_values_from_regular_frame(frame_idx)
            roll_value_string += f"| {roll1} | {roll2} "

        last1, last2, last3 = self.__get_roll_values_from_last_frame()
        roll_value_string += f"| {last1} | {last2} | {last3} |"

        return roll_value_string

    # TODO: hier nicht mit idx arbeiten, das geht auch sauberer.
    def __get_roll_values_from_regular_frame(self, frame_idx: int) -> tuple[str, str]:
        roll1 = ' '
        roll2 = ' '
        if frame_idx < len(self._frame_rolls):
            roll_values = self._frame_rolls[frame_idx][0]
            if len(roll_values) == 1:
                if roll_values[0] == 10:
                    roll2 = 'X'
                else:
                    roll1 = str(roll_values[0])
            else:
                if sum(roll_values) == 10:
                    roll1 = str(roll_values[0])
                    roll2 = '/'
                else:
                    roll1, roll2 = roll_values
        return roll1, roll2

    # TODO: surely there is a nicer way!
    def __get_roll_values_from_last_frame(self) -> tuple[str, str, str]:
        roll1 = ' '
        roll2 = ' '
        roll3 = ' '
        if len(self._frame_rolls) == 10:
            rolls = self._frame_rolls[9][0]

            if rolls[0] == 10:
                roll1 = 'X'
            else:
                roll1 = str(rolls[0])

            if len(rolls) > 1:
                if rolls[1] == 10:
                    roll2 = 'X'
                elif rolls[0] + rolls[1] == 10 and rolls[1] != 0:
                    roll2 = '/'
                else:
                    roll2 = str(rolls[1])

            if len(rolls) > 2:
                if rolls[2] == 10:
                    roll3 = 'X'
                elif rolls[1] + rolls[2] == 10 and rolls[2] != 0:
                    roll3 = '/'
                else:
                    roll3 = str(rolls[2])

        return roll1, roll2, roll3

    def __draw_score(self) -> str:
        scores = self.__get_scores()
        while len(scores) < 10:
            scores.append('')

        # TODO: Can we do this in a loop?
        score_string = f"| {scores[0]:>4}  | {scores[1]:>4}  | {scores[2]:>4}  | {scores[3]:>4}  " \
                       f"| {scores[4]:>4}  | {scores[5]:>4}  | {scores[6]:>4}  | {scores[7]:>4}  " \
                       f"| {scores[8]:>4}  |   {scores[9]:>4}    |"

        return score_string

    def __get_scores(self) -> list[str]:
        scores = []
        total_score = 0
        for frame in self._frame_rolls:
            if frame[1] is not None:
                total_score += frame[1]
                scores.append(str(total_score))  # cast to string here, so we pad the list with '' in __draw_score
        return scores

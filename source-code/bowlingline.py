import frame
import rollgenerator


class BowlingLine:
    """
    A BowlingLine represents a full game of bowling.
    A BowlingLine is filled with ten Frames: nine RegularFrames and one LastFrame.
    The list of Frames (self.__frames) starts out empty. New Frames will be appended as needed.
    A BowlingLine requires a RollGenerator object which generates roll values
        (= the amount of pins knocked down with one ball) one by one.
    Each roll value is passed to each non-full Frame in self.__frames.
    The BowlingLine will add up all Frame scores to calculate the final score.
    """
    def __init__(self, roll_generator: rollgenerator.RollGenerator):
        self.__roll_generator = roll_generator
        self.__frames = []
        self.__run_bowling_game()

    def __add_new_frame(self):
        # Adds a new RegularFrame if no other Frame accepts regular rolls.
        # Adds a new LastFrame instead if it's the tenth Frame.
        if self.__frames and not self.__frames[-1].regular_rolls_are_full():
            return

        num_of_frames = len(self.__frames)
        if num_of_frames < 9:
            self.__frames.append(frame.RegularFrame())
        elif num_of_frames == 9:
            self.__frames.append(frame.LastFrame())

    def __send_roll_to_frames(self, roll):
        self.__add_new_frame()
        for a_frame in self.__frames:
            if not a_frame.is_full():
                a_frame.receive_a_roll(roll)

    def __run_bowling_game(self):
        while not self.__is_game_over():
            roll = self.__roll_generator.get_next_roll()
            self.__send_roll_to_frames(roll)

    def __is_game_over(self) -> bool:
        # The game is over when all ten Frames are completely full.
        return len(self.__frames) == 10 and self.__frames[-1].is_full()

    def get_final_score(self):
        final_score = sum(filled_frame.get_total_score() for filled_frame in self.__frames)
        return final_score

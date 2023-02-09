import time

import bowlingframe
import rollgenerator
import scoreoutput


class BowlingLine:
    """
    A BowlingLine represents a full game of bowling.
    A BowlingLine is filled with ten Frames: nine RegularFrames and one LastFrame.
    The list of Frames (self.__frames) starts out empty. New Frames will be appended as needed.
    A BowlingLine requires a RollGenerator object which generates roll values
        (= the amount of pins knocked down with one ball) one by one.
    Each roll value is passed to each non-full Frame in self.__frames.
    The BowlingLine will add up all Frame scores to calculate the final score.
    The BowlingLine can pass its Frames' roll values and scores to an out ConsoleOutput object to generate output.
    """
    def __init__(self, roll_generator: rollgenerator.RollGenerator):
        self.__roll_generator = roll_generator
        self.__frames = []
        self.__output_methods = set()

    def add_output_method(self, output: scoreoutput.ConsoleOutput):
        self.__output_methods.add(output)

    def remove_output_method(self):
        pass

    def generate_output(self):
        output_data = self.__get_output_data()
        for output in self.__output_methods:
            output.generate_output(output_data)

    def start_bowling_game(self):
        self.__run_bowling_game()

    def __get_output_data(self):
        output_data = []
        for frame in self.__frames:
            rolls = frame.regular_rolls[:]
            score = frame.get_total_score()
            output_data.append((rolls, score))
        return output_data

    def __add_new_frame(self):
        # Adds a new RegularFrame if no other Frame accepts regular rolls.
        # Adds a new LastFrame instead if it's the tenth Frame.
        if self.__frames and not self.__frames[-1].regular_rolls_are_full():
            return

        num_of_frames = len(self.__frames)
        if num_of_frames < 9:
            self.__frames.append(bowlingframe.RegularFrame())
        elif num_of_frames == 9:
            self.__frames.append(bowlingframe.LastFrame())

    def __send_roll_to_frames(self, roll):
        self.__add_new_frame()
        for frame in self.__frames:
            if not frame.is_full():
                frame.receive_a_roll(roll)

    def __run_bowling_game(self):
        while not self.__is_game_over():
            roll = self.__roll_generator.get_next_roll()
            self.__send_roll_to_frames(roll)
            self.generate_output()

    def __is_game_over(self) -> bool:
        # The game is over when all ten Frames are completely full.
        return len(self.__frames) == 10 and self.__frames[-1].is_full()

    def get_final_score(self):
        final_score = sum(frame.get_total_score() for frame in self.__frames)
        return final_score


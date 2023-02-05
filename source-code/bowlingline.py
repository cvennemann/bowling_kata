import frame
import rollgenerator


class BowlingLine:
    def __init__(self, roll_gen: rollgenerator.Rollgenerator):
        self.__roll_generator = roll_gen
        self.__frames = []

    def send_roll_to_frames(self, roll):
        self.__add_new_frame()

        for a_frame in self.__frames:
            if not a_frame.is_full():
                a_frame.receive_a_roll(roll)

    def __add_new_frame(self):
        if not self.__frames or self.__frames[-1].frame_is_full():
            num_of_frames = len(self.__frames)
            if num_of_frames < 9:
                self.__frames.append(frame.RegularFrame())
            elif num_of_frames == 9:
                self.__frames.append(frame.LastFrame())

    def run_bowling_game(self):
        roll_gen = self.__roll_generator.get_roll_generator()

        while not self.__game_over():
            roll = next(roll_gen)
            print(roll)
            self.send_roll_to_frames(roll)

    def __game_over(self) -> bool:
        return len(self.__frames) == 10 and self.__frames[-1].is_full()

    def get_final_score(self):
        self.run_bowling_game()

        final_score = 0
        for finished_frame in self.__frames:
            final_score += finished_frame.get_total_score()
            # print(final_score)
        return final_score

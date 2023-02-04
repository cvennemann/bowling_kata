import frame
import rollgenerator


class BowlingLine:
    def __init__(self, roll_gen: rollgenerator.Rollgenerator):
        self.__roll_generator = roll_gen

    def get_final_score(self) -> int:
        return -100
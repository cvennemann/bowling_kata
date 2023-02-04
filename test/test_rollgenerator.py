from unittest import TestCase
from rollgenerator import StringToRollGenerator


class TestRollGenerator(TestCase):
    def test_yield_next_roll(self):
        test_string = '5/ -5 4/ -- 6/ 25 7/ X 12 34'
        goal_list = [5, 5, 0, 5, 4, 6, 0, 0, 6, 4, 2, 5, 7, 3, 10, 1, 2, 3, 4]

        roll_gen = StringToRollGenerator(test_string)
        test_list = [roll for roll in roll_gen.yield_next_roll()]

        self.assertEquals(test_list, goal_list)



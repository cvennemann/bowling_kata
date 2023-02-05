from unittest import TestCase
from rollgenerator import StringToRollGenerator


class TestStringToRollGenerator(TestCase):
    def test_get_next_roll(self):
        print('Testing StringToRollGenerator.get_roll_generator()')
        test_string = '5/ -5 4/ -- 6/ 25 7/ X 12 34'
        goal_list = [5, 5, 0, 5, 4, 6, 0, 0, 6, 4, 2, 5, 7, 3, 10, 1, 2, 3, 4]

        roll_gen = StringToRollGenerator(test_string)
        test_list = [roll for roll in roll_gen.get_roll_generator()]

        self.assertEqual(test_list, goal_list)

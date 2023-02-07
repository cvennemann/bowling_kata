from unittest import TestCase
from rollgenerator import StringToRollGenerator


class TestStringToRollGenerator(TestCase):
    def test_get_next_roll(self):
        print('Testing StringToRollGenerator.get_next_roll()')
        test_string = '5/ -5 4/ -F 6/ 25 7/ X 12 34'
        goal_list = [5, 5, 0, 5, 4, 6, 0, 0, 6, 4, 2, 5, 7, 3, 10, 1, 2, 3, 4]

        roll_gen = StringToRollGenerator(test_string)

        for number in goal_list:
            self.assertEqual(number, roll_gen.get_next_roll())

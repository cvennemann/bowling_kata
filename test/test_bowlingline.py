from unittest import TestCase
from rollgenerator import StringToRollGenerator
from bowlingline import BowlingLine


class TestBowlingLine(TestCase):
    def test_get_final_score(self):
        print('Testing BowlingLine.get_final_score()')

        # simple test
        print('12 34 12 34 12 34 12 34 12 34')
        self.roll_gen1 = StringToRollGenerator('12 34 12 34 12 34 12 34 12 34')
        self.bowling_line1 = BowlingLine(self.roll_gen1)
        self.assertEqual(self.bowling_line1.get_final_score(), 50)

        # all strikes
        print('X X X X X X X X X X X X')
        self.roll_gen1 = StringToRollGenerator('X X X X X X X X X X X X')
        self.bowling_line1 = BowlingLine(self.roll_gen1)
        self.assertEqual(self.bowling_line1.get_final_score(), 300)

        # all 9-
        print('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-')
        self.roll_gen2 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- 9- 9-')
        self.bowling_line2 = BowlingLine(self.roll_gen2)
        self.assertEqual(self.bowling_line2.get_final_score(), 90)

        # all spares
        print('-/ 1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9/5')
        self.roll_gen3 = StringToRollGenerator('-/ 1/ 2/ 3/ 4/ 5/ 6/ 7/ 8/ 9/5')
        self.bowling_line3 = BowlingLine(self.roll_gen3)
        self.assertEqual(self.bowling_line3.get_final_score(), 150)

        # all miss
        print('-- -- -- -- -- -- -- -- -- --')
        self.roll_gen4 = StringToRollGenerator('-- -- -- -- -- -- -- -- -- --')
        self.bowling_line4 = BowlingLine(self.roll_gen4)
        self.assertEqual(self.bowling_line4.get_final_score(), 0)

        # frame 9 strike into frame 10 open frame
        print('9- 9- 9- 9- 9- 9- 9- 9- X 35')
        self.roll_gen5 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- X 35')
        self.bowling_line5 = BowlingLine(self.roll_gen5)
        self.assertEqual(self.bowling_line5.get_final_score(), 98)

        # frame 9 Strike into frame 10 spare
        print('9- 9- 9- 9- 9- 9- 9- 9- X 3/5')
        self.roll_gen6 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- X 3/5')
        self.bowling_line6 = BowlingLine(self.roll_gen6)
        self.assertEqual(self.bowling_line6.get_final_score(), 107)

        # frame 9 Strike into frame 10 miss
        print('9- 9- 9- 9- 9- 9- 9- 9- X -3')
        self.roll_gen7 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- X -3')
        self.bowling_line7 = BowlingLine(self.roll_gen7)
        self.assertEqual(self.bowling_line7.get_final_score(), 88)

        # frame 9 Strike into frame 10 spare into strike
        print('9- 9- 9- 9- 9- 9- 9- 9- X 3/X')
        self.roll_gen8 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- X 3/X')
        self.bowling_line8 = BowlingLine(self.roll_gen8)
        self.assertEqual(self.bowling_line8.get_final_score(), 112)

        # frame 9 spare into frame 10 strike
        print('9- 9- 9- 9- 9- 9- 9- 9- 9/ X43')
        self.roll_gen9 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- 9/ X43')
        self.bowling_line9 = BowlingLine(self.roll_gen9)
        self.assertEqual(self.bowling_line9.get_final_score(), 109)

        # frame 9 spare into frame 10 spare
        print('9- 9- 9- 9- 9- 9- 9- 9- 9/ 7/3')
        self.roll_gen10 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- 9/ 7/3')
        self.bowling_line10 = BowlingLine(self.roll_gen10)
        self.assertEqual(self.bowling_line10.get_final_score(), 102)

        # frame 9 spare into frame 10 open frame
        print('9- 9- 9- 9- 9- 9- 9- 9- 9/ 25')
        self.roll_gen11 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- 9/ 25')
        self.bowling_line11 = BowlingLine(self.roll_gen11)
        self.assertEqual(self.bowling_line11.get_final_score(), 91)

        # frame 9 spare into frame 10 miss
        print('9- 9- 9- 9- 9- 9- 9- 9- 9/ --')
        self.roll_gen12 = StringToRollGenerator('9- 9- 9- 9- 9- 9- 9- 9- 9/ --')
        self.bowling_line12 = BowlingLine(self.roll_gen12)
        self.assertEqual(self.bowling_line12.get_final_score(), 82)

        # regular frame strikes into miss, open, spare
        print('X -3 X -- X 45 X 4/ 23 34')
        self.roll_gen13 = StringToRollGenerator('X -3 X -- X 45 X 4/ 23 34')
        self.bowling_line13 = BowlingLine(self.roll_gen13)
        self.assertEqual(self.bowling_line13.get_final_score(), 98)

        # regular frame spare into miss, open, strike
        print('5/ -5 4/ -- 6/ 25 7/ X 12 34')
        self.roll_gen14 = StringToRollGenerator('5/ -5 4/ -- 6/ 25 7/ X 12 34')
        self.bowling_line14 = BowlingLine(self.roll_gen14)
        self.assertEqual(self.bowling_line14.get_final_score(), 87)

        # tenth frame strike into open frame
        print('-- -- -- -- -- -- -- -- -- X--')
        self.roll_gen15 = StringToRollGenerator('-- -- -- -- -- -- -- -- -- X--')
        self.bowling_line15 = BowlingLine(self.roll_gen15)
        self.assertEqual(self.bowling_line15.get_final_score(), 10)

        # tenth frame strike into miss spare
        print('-- -- -- -- -- -- -- -- -- X-/')
        self.roll_gen16 = StringToRollGenerator('-- -- -- -- -- -- -- -- -- X-/')
        self.bowling_line16 = BowlingLine(self.roll_gen16)
        self.assertEqual(self.bowling_line16.get_final_score(), 20)

        # tenth frame spare into miss
        print('-- -- -- -- -- -- -- -- -- -/-')
        self.roll_gen17 = StringToRollGenerator('-- -- -- -- -- -- -- -- -- -/-')
        self.bowling_line17 = BowlingLine(self.roll_gen17)
        self.assertEqual(self.bowling_line17.get_final_score(), 10)

        # tenth frame spare into strike
        print('-- -- -- -- -- -- -- -- -- -/X')
        self.roll_gen18 = StringToRollGenerator('-- -- -- -- -- -- -- -- -- -/X')
        self.bowling_line18 = BowlingLine(self.roll_gen18)
        self.assertEqual(self.bowling_line18.get_final_score(), 20)

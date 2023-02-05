from unittest import TestCase
from frame import RegularFrame, LastFrame


class TestRegularFrame(TestCase):
    def setUp(self):
        # double miss
        self.reg_frame0 = RegularFrame()
        self.reg_frame0.receive_a_roll(0)
        self.reg_frame0.receive_a_roll(0)

        # open frame
        self.reg_frame1 = RegularFrame()
        self.reg_frame1.receive_a_roll(4)
        self.reg_frame1.receive_a_roll(5)

        # spare
        self.reg_frame2 = RegularFrame()
        self.reg_frame2.receive_a_roll(4)
        self.reg_frame2.receive_a_roll(6)
        self.reg_frame2.receive_a_roll(5)

        # strike
        self.reg_frame3 = RegularFrame()
        self.reg_frame3.receive_a_roll(10)
        self.reg_frame3.receive_a_roll(3)
        self.reg_frame3.receive_a_roll(5)

    def test_get_base_score(self):
        print('Testing RegularFrame.get_base_score()')
        self.assertEqual(self.reg_frame0.get_base_score(), 0)
        self.assertEqual(self.reg_frame1.get_base_score(), 9)
        self.assertEqual(self.reg_frame2.get_base_score(), 10)
        self.assertEqual(self.reg_frame3.get_base_score(), 10)

    def test_get_bonus_score(self):
        print('Testing RegularFrame.get_bonus_score()')
        self.assertEqual(self.reg_frame0.get_bonus_score(), 0)
        self.assertEqual(self.reg_frame1.get_bonus_score(), 0)
        self.assertEqual(self.reg_frame2.get_bonus_score(), 5)
        self.assertEqual(self.reg_frame3.get_bonus_score(), 8)

    def test_get_total_score(self):
        print('Testing RegularFrame.get_total_score()')
        self.assertEqual(self.reg_frame0.get_total_score(), 0)
        self.assertEqual(self.reg_frame1.get_total_score(), 9)
        self.assertEqual(self.reg_frame2.get_total_score(), 15)
        self.assertEqual(self.reg_frame3.get_total_score(), 18)


class TestLastFrame(TestCase):
    def setUp(self):
        # double miss
        self.last_frame0 = LastFrame()
        self.last_frame0.receive_a_roll(0)
        self.last_frame0.receive_a_roll(0)

        # open frame
        self.last_frame1 = LastFrame()
        self.last_frame1.receive_a_roll(4)
        self.last_frame1.receive_a_roll(5)

        # spare
        self.last_frame2 = LastFrame()
        self.last_frame2.receive_a_roll(4)
        self.last_frame2.receive_a_roll(6)
        self.last_frame2.receive_a_roll(5)

        # strike
        self.last_frame3 = LastFrame()
        self.last_frame3.receive_a_roll(10)
        self.last_frame3.receive_a_roll(3)
        self.last_frame3.receive_a_roll(5)

        # 3 strikes
        self.last_frame4 = LastFrame()
        self.last_frame4.receive_a_roll(10)
        self.last_frame4.receive_a_roll(10)
        self.last_frame4.receive_a_roll(10)

    def test_get_base_score(self):
        print("Testing LastFrame.get_base_score()")
        self.assertEqual(self.last_frame0.get_base_score(), 0)
        self.assertEqual(self.last_frame1.get_base_score(), 9)
        self.assertEqual(self.last_frame2.get_base_score(), 15)
        self.assertEqual(self.last_frame3.get_base_score(), 18)
        self.assertEqual(self.last_frame4.get_base_score(), 30)

    def test_get_bonus_score(self):
        print("Testing LastFrame.get_bonus_score()")
        self.assertEqual(self.last_frame0.get_bonus_score(), 0)
        self.assertEqual(self.last_frame1.get_bonus_score(), 0)
        self.assertEqual(self.last_frame2.get_bonus_score(), 0)
        self.assertEqual(self.last_frame3.get_bonus_score(), 0)
        self.assertEqual(self.last_frame4.get_bonus_score(), 0)

    def test_get_total_score(self):
        print("Testing LastFrame.get_total_score()")
        self.assertEqual(self.last_frame0.get_total_score(), 0)
        self.assertEqual(self.last_frame1.get_total_score(), 9)
        self.assertEqual(self.last_frame2.get_total_score(), 15)
        self.assertEqual(self.last_frame3.get_total_score(), 18)
        self.assertEqual(self.last_frame4.get_total_score(), 30)

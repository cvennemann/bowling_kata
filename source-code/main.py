import bowlingline
import rollgenerator
import scoreoutput


if __name__ == '__main__':
    roll_gen1 = rollgenerator.StringToRollGenerator('5/ -5 4/ -- 6/ 25 7/ X 12 34')
    roll_gen2 = rollgenerator.InputRollGenerator()

    output1 = scoreoutput.TerminalOutput()

    bowling_line1 = bowlingline.BowlingLine(roll_gen1)

    bowling_line1.add_output_method(output1)
    bowling_line1.start_bowling_game()

# Bowling kata

### Description:
    - input: string representing a full game of valid rolls
    - output: total bowling score
    
    NOT part of the original kata but maybe in the future:
    - check for valid rolls
    - check for correct number of rolls and frames
    - provide scores for intermediate frames

### Entities of the Bowling game:
    - roll: the number of pins knocked down by one ball
    - line: a full game of bowling consisting of ten frames
    - frame:
        . regular frame: a regular frame has a length of either two tries in case of an open frame or spare,
                         or one try in case of a strike.
                         In case of a spare or strike, the next one or two rolls from the following frame(s)
                         are added to this frame's score as well.
        . 10th frame: the tenth frame has a length of up to three tries in case of a strike or spare,
                         and two tries otherwise.

### Basic idea:
        The BowlingLine gets roll values one by one from a RollGenerator and passes them on to the current Frame.
        Each Frame will track its own tries and score and will inform the BowlingLine when it is full.
        The BowlingLine will then pass the next roll value to the next Frame until all ten Frames are filled.
        The BowlingLine summs up all Frame-scores and returns the final score.

        Bonus: different ways of generating rolls, e.g. user input


        +------------+          +----------------+            +-----------------+
        | <abstract> |--------<>|  BowlingLine   |<>----------|    <abstract>   |
        |   Frame    |          |                |            |  RollGenerator  |
        +------^-----+          +----------------+            +--------^--------+
              /_\                                                     /_\
               |                                                       |
           ____|____________________                           ________|_______________________ _ _ _ 
           |                       |                           |                              |
           |                       |                           |                              |
       +----------------+    +--------------+       +-------------------------+    +----------------------+
       |  RegularFrame  |    |  LastFrame   |       |  StringToRollGenerator  |    |  [...]RollGenerator  |
       |                |    |              |       |                         |    |                      |
       +----------------+    +--------------+       +-------------------------+    +----------------------+
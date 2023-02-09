# Bowling kata
	
	This is my exercise / attempt at solving the bowling kata using test driven development and object orientation.
	
	Source: https://codingdojo.org/kata/Bowling/

### Description:

	Core Features:
    - [DONE] input: string representing a full game of valid rolls
    - [DONE] output: total bowling score
    
    NOT part of the original kata but maybe in the future:
    - check for valid rolls
    - check for correct number of rolls and frames
    - [DONE] provide scores for intermediate frames
	
	What I think would be fun:
	- [DONE] ASCII style console output similar to a traditional bowling core sheet
	- [DONE] console user input
	- can track multiple games 
	- for multiple players

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
        The BowlingLine gets roll values one by one from a RollGenerator and passes them on to its list of Frames.
        Each Frame will accept rolls and calculate its score until it is full. A new Frame will be added if necessary.
		When the tenth Frame is full, the game is over.
		For output, the BowlingLine can take the Frames' scores and passes them on to one or several ScoreOutput classes.
		
		
		                          +---------------+        +-----------------+
		                          |  <abstract>   |<|------|  ConsoleOutput  |
		                          |  ScoreOutput  |        |                 |
		                          +-------+-------+        +-----------------+
		                                  |
		                                  |
                                          |
                                         \-/
        +------------+          +---------v------+            +-----------------+
        | <abstract> |--------<>|  BowlingLine   |<>----------|    <abstract>   |
        |   Frame    |          |                |            |  RollGenerator  |
        +------^-----+          +----------------+            +--------^--------+
              /_\                                                     /_\
               |                                                       |
           ____|____________________                           ________|_______________________ 
           |                       |                           |                              |
           |                       |                           |                              |
       +----------------+    +--------------+       +-------------------------+    +----------------------+
       |  RegularFrame  |    |  LastFrame   |       |  StringToRollGenerator  |    |  InputRollGenerator  |
       |                |    |              |       |                         |    |                      |
       +----------------+    +--------------+       +-------------------------+    +----------------------+
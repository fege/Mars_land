# Mars land

We are sending a robot to Mars to give candies to Martians. For this purpose there is  an agreement with 
NASA. The robotic rover are going to land on a plateau on Mars. This plateau, which is curiously 
rectangular, limited (9,9) and represented in a grid, must be navigated by the rover that can give
candies to all Martians. The position and location of the rover is represented by a combination of x and y 
co-‐ordinates and a letter representing one of the four cardinal compass points (N, S, E, W).
An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing
North. In order to drive the rover around Mars, NASA sends a simple string of letters. The possible letters are 
'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving the 
rover from its current position. 'M' means move forward one grid point, and maintain the same heading. 
Assume that the square directly North from (x, y) is (x, y+1).

Input: As input you get 2 strings, the first one is the position where the rover has landed; the second is the
sequence of movements the rover has to perform so that Tiffi can hand out the candies.

Output: As output you have to define the rover’s last position and orientation, so we can collect and bring it 
back to earth to get more candies.

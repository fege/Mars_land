'''
Created on 09.12.2014

@author: Federico
'''

POSSIBLE_POSITIONS = tuple((x, y) for x in range(0, 10) for y in range(0, 10))
VERSE = {
         'E': {'L': 'N', 'R': 'S'},
         'N': {'L': 'W', 'R': 'E'},
         'W': {'L': 'S', 'R': 'N'},
         'S': {'L': 'E', 'R': 'W'}
         }
MOVES = {
         'E': (1, 0),
         'N': (0, 1),
         'S': (0, -1),
         'W': (-1, 0),
         }


class NotStringError(ValueError): pass
class PositionOutBoard(ValueError): pass
class NotPossibleMove(ValueError): pass
class NotValidPoint(ValueError): pass

def find_martians(pos, path):
    """
    function to check the input, call the function for moving the rover and return the final position 
    """
    if not isinstance(pos,str) or not isinstance(path,str):
        raise NotStringError('for input just 2 strings are allowed')
    if len(pos) != 3 or pos == '':
        raise NotValidPoint(pos, 'position is mandatory and it is xyd where x and y is 0..9')
    position = (int(pos[0]),int(pos[1]))
    if position not in POSSIBLE_POSITIONS:
        raise PositionOutBoard(position, 'is not a valid position')
    verse = pos[2]
    if verse not in VERSE.keys():
        raise NotValidPoint(VERSE.keys(), 'are the only verses accepted')
    final_pos = move(position, verse, path)
    return ''.join([str(item) for sub_i in final_pos for item in sub_i])

def move(pos, verse, path):
    """
    recursive function to determine the next point on the grid where tiffi wants to go
    """
    if pos not in POSSIBLE_POSITIONS:
        raise PositionOutBoard(pos, 'is not a valid position')
    if len(path) == 0:
        return pos, verse
    else:
        if path[0] == 'L' or path[0]  == 'R':
            """calculate new verse"""
            verse = VERSE[verse][path[0]]
        elif path[0] == 'M':
            """next position on the grid"""
            pos = tuple(map(lambda x, y: x + y, MOVES[verse], pos))
        else:
            raise NotPossibleMove(path[0], 'is not a valid move')
        return move(pos,verse,path[1:])

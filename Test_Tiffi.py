'''
Created on 09.12.2014

@author: Federico
'''
import unittest
import Tiffi


class Test(unittest.TestCase):

    def testOutBoard(self):
        """Test for check when the position is outside the board"""
        values = [('00N', 'MMMMMMMMMM'), ('99S', 'MMMMMMMMMM'), \
            ('00E', 'MMMMMMMMMM'), ('99W', 'MMMMMMMMMM'), \
            ('99S', 'MMMMLMMMMM'), ('00E', 'MMMMRMMMMM'), \
            ('00N', 'MMMMLMMMMM'), ('99W', 'MMMMRMMMMM'), ('44N', 'MMMMMM')]
        for pos, path in values:
            self.assertRaises(Tiffi.PositionOutBoard, Tiffi.find_martians, pos, path)

    def testBoardEdge(self):
        """Test to check the internal edge of the board"""
        values = [('00N', 'MMMMMMMMM', '09N'), ('99S', 'MMMMMMMMM', '90S'), \
            ('00E', 'MMMMMMMMM', '90E'), ('99W', 'MMMMMMMMM', '09W'), \
            ('99S', 'MMMMLLMMMM', '99N'), ('00E', 'MMMMRRMMMM', '00W'),\
            ('00N', 'MMMMLLMMMM', '00S'), ('99W', 'MMMMRRMMMM', '99E')]
        for pos, path, expected in values:
            result = Tiffi.find_martians(pos, path)
            self.assertEqual(expected, result)

    def testInvalidPoint(self):
        """Test invalid landing point and direction"""
        values = [('410N', 'LMMMRRM'), ('', 'LMMMRRM'), ('23', 'LMMMRRM'), \
                  ('11F', 'LMMMRRM')]
        for pos, path in values:
            self.assertRaises(Tiffi.NotValidPoint, Tiffi.find_martians, pos, path)

    def testInvalidMove(self):
        """Test invalid move"""
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        alphabet = [x for x in alphabet if x not in ['M', 'L', 'R']]
        str_numbers = str(range(10))
        for move in alphabet:
            self.assertRaises(Tiffi.NotPossibleMove, Tiffi.find_martians, '00N', move)
        for move in str_numbers:
            self.assertRaises(Tiffi.NotPossibleMove, Tiffi.find_martians, '00N', move)

    def testNotStr(self):
        """Test not string as input"""
        numbers = range(10)
        for move in numbers:
            self.assertRaises(Tiffi.NotStringError, Tiffi.find_martians, '00N', move)
        for pos in numbers:
            self.assertRaises(Tiffi.NotStringError, Tiffi.find_martians, pos, 'LMMMRRM')

    def testHappyPath(self):
        """Test Happy Path"""
        know_values = [('44N', '', '44N'), ('44N', 'LMMMRRM', '24E'), \
                       ('33E', 'LMRRMLLMRRMMMM', '30S')]
        for pos, path, expected in know_values:
            result = Tiffi.find_martians(pos, path)
            self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()

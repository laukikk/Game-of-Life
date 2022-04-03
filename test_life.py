import numpy as np
import unittest
import game_of_life as life
import json

f = open('data.json')
data = json.load(f)

sol_f = open('solutions.json')
solutions = json.load(sol_f)

class TestGameOfLife(unittest.TestCase):

    def test_life_still(self):
        global data, solutions
        self.assertEqual(life.runGame(data['still']), solutions['still'])

    def test_life_oscillators(self):
        global data, solutions
        self.assertEqual(life.runGame(data['oscs']), solutions['oscs'])
        self.assertEqual(life.runGame(data['beacon']), solutions['beacon'])
    
    def test_life_spaceships(self):
        global data, solutions
        self.assertEqual(life.runGame(data['glider']), solutions['glider'])
        self.assertEqual(life.runGame(data['LWSS']), solutions['LWSS'])
        self.assertEqual(life.runGame(data['MWSS']), solutions['MWSS'])
        self.assertEqual(life.runGame(data['HWSS']), solutions['HWSS'])


if __name__ == '__main__':
    
    unittest.main()
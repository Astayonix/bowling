import unittest
import bowling

class BowlingGameUnitTests(unittest.TestCase):

    def test_startGame(self):
        myGame = bowling.BowlingGame(3, True)
    
    # def test_showLane(self):
    #     assert()

if __name__ == "__main__":
    unittest.main()
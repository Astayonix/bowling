import unittest
import bowling

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.myGame = bowling.BowlingGame()

    def test_startGame(self):
        self.myGame

    def test_numPlayers(self):
        self.assertIn(0, self.myGame.num_players)

    def test_bumpersUpDown(self):
        self.assertTrue(self.myGame.bumpersUpDown, True)

    def test_showLane(self):
        self.myGame.showLane()

if __name__ == "__main__":
    unittest.main()
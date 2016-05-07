from random import choice

class BowlingGame(object):

    lane = range(10)
    frames = 10
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False

    def __init__(self, num_players, bumpers):
        self.num_players = num_players
        self.bumpers = bumpers

    def showLane(self):
        """Shows the current configuration of the pins in the lane"""
        print "||  %s %s %s %s  ||" % (self.lane[0],self.lane[1],self.lane[2],self.lane[3])
        print "||   %s %s %s   ||" % (self.lane[4], self.lane[5], self.lane[6])
        print "||    %s %s    ||" % (self.lane[7], self.lane[8])
        print "||     %s     ||" % (self.lane[9])

myGame = BowlingGame(3, True)

print myGame.showLane()
# print myGame.bumpers
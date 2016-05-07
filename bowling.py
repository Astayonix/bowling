from random import choice

class BowlingAlley(object):

    lane = range(10)
    frames = 10
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False

    def __init__(self, num_players, bumpers):
        self.num_players = num_players
        self.bumpers = bumpers
        # pins = range(10)
    def showLane(self):
        print "||  %s %s %s %s  ||" % (self.lane[0],self.lane[1],self.lane[2],self.lane[3])
        print "||   %s %s %s   ||" % (self.lane[4], self.lane[5], self.lane[6])
        print "||    %s %s    ||" % (self.lane[7], self.lane[8])
        print "||     %s     ||" % (self.lane[9])

myGame = BowlingAlley(3, True)

# print myGame.pins
# print myGame.frames
print myGame.showLane()
print myGame.bumpers
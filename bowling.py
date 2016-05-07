from random import choice

class BowlingGame(object):

    pins_in_lane = range(10)
    total_frames = 10
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False
    num_players = []

    def __init__(self, num_players):
        """Intial configuration of the bowling game"""
        self.num_players = range(num_players)

    def greetingUser(self):
        """Greets the user"""
        print "Welcome to the Bowling Alley!\nBefore we get started, I need to know if you want to use bumpers."

    def bumpersUpDown(self):
        """Sets bumper use to either True or False"""
        userinput = raw_input("Type 'True' or 'False' to indicate the use of bumpers >>> ")
        valid_input = False
        while valid_input == False:
            try:
                if userinput == 'True':
                    self.bumpers = True
                    print "Great! Bumpers are ON.\nNow, lace up your shoes, grab a ball, and I'll meet you at the lane!"
                    valid_input = True
                elif userinput == 'False':
                    self.bumpers = False
                    print "Great! Bumpers are OFF.\nNow, lace up your shoes, grab a ball, and I'll meet you at the lane!"
                    valid_input = True
                else:
                    userinput = raw_input("Invalid input.  Please type 'True' or 'False' >>> ")
            except ValueError:
                userinput = raw_input("Invalid input.  Please type 'True' or 'False' >>> ")

    def showLane(self):
        """Shows the current configuration of the pins in the lane"""
        if self.bumpers == True:
            print "Here is what the pins currently look line in the lane."
            print "||}  %s %s %s %s  {||" % (self.pins_in_lane[0],self.pins_in_lane[1],self.pins_in_lane[2],self.pins_in_lane[3])
            print "||}   %s %s %s   {||" % (self.pins_in_lane[4], self.pins_in_lane[5], self.pins_in_lane[6])
            print "||}    %s %s    {||" % (self.pins_in_lane[7], self.pins_in_lane[8])
            print "||}     %s     {||" % (self.pins_in_lane[9])
        else:
            print "Here is what the pins currently look line in the lane."
            print "{||  %s %s %s %s  ||}" % (self.pins_in_lane[0],self.pins_in_lane[1],self.pins_in_lane[2],self.pins_in_lane[3])
            print "{||   %s %s %s   ||}" % (self.pins_in_lane[4], self.pins_in_lane[5], self.pins_in_lane[6])
            print "{||    %s %s    ||}" % (self.pins_in_lane[7], self.pins_in_lane[8])
            print "{||     %s     ||}" % (self.pins_in_lane[9])

    def throwBall(self):
        while throws_per_frame > 0:
            print throws_per_frame

myGame = BowlingGame(1)
myGame.greetingUser()
myGame.bumpersUpDown()
myGame.showLane()
myGame.throwBall()
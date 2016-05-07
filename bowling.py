from random import choice

class BowlingGame(object):

    pins_in_lane = range(10)
    total_frames = range(10)
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False
    num_players = 1

    # def __init__(self, num_players):
    #     """Intial configuration of the bowling game"""
    #     self.num_players = range(num_players)

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

    def frameHandler(self):
        """Keeps track of the number of frames remaining in the game"""
        while self.total_frames:
            print "This is frame %s of 10" % (self.total_frames[0]+1)
            for frame in self.total_frames:
                print frame
                self.throwBall()
            self.total_frames.pop(0)

    def throwBall(self):
        """Determines if the ball hits the pins in the lane or not and decrements the number of balls left to roll in the current frame"""
        while self.throws_per_frame:
            self.throws_per_frame -= 1
            hit_pins = choice([True, False])
            if hit_pins == True:
                print "The ball hits the pins!"
                return True
            elif hit_pins == False and self.bumpers == False:
                print "Oh no! A gutter ball!"
            else:
                print "Somehow, the ball missed the pins entirely!"

    def pinsHit(self):
        """Determines which pins were hit and re-draws what the pins look like in the lane"""
        self.throwBall()
        hit = self.throwBall()
        if hit == True:
            num_of_pins_to_fall = choice(len(self.pins_in_lane))
            print num_of_

myGame = BowlingGame()
myGame.greetingUser()
myGame.bumpersUpDown()
myGame.showLane()
myGame.frameHandler()
myGame.pinsHit()
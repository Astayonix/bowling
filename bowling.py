from random import choice, randint, sample

class BowlingGame(object):

    pins_in_lane = range(10)
    total_frames = range(10)
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False
    num_players = 1

    def __init__(self, name):
        self.name = name

    def userGreeting(self):
        """Greets the user"""
        print "Welcome to the Bowling Alley, %s!\nBefore we get started, I need to know if you want to use bumpers." % (self.name)
        self.bumpersUpDown()

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
        self.frameHandler()

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
        total_score_list = []
        for frame in self.total_frames:
            print "This is frame %s of 10" % (frame+1)
            self.showLane()
            a_round = self.throwBall()
            total_score_list.append(a_round)
            # self.showLeaderboard()
            self.resetLane()
        return total_score_list
        # self.resetBowlingGame()
            # print frame

    def throwBall(self):
        """Determines if the ball hits the pins in the lane or not and decrements the number of balls left to roll in the current frame"""
        running_score_this_frame = 0
        this_throw_scores = [] #[first throw, second throw, special scoring type]
        while self.throws_per_frame:
            hit_pins = choice([True, False])
            if hit_pins == True:
                print "The ball hits the pins!"
                remaining_pins = [pin for pin in self.pins_in_lane if pin != '/']
                pins_knocked_over = sample(remaining_pins, randint(1,len(remaining_pins)))
                if pins_knocked_over != []:
                    for pin in pins_knocked_over:
                        self.pins_in_lane[pin] = '/'
                    fallen_pins_this_throw = len(pins_knocked_over)
                    running_score_this_frame += fallen_pins_this_throw
                    self.showLane()
                    if fallen_pins_this_throw == 10:
                        this_throw_scores.append(fallen_pins_this_throw)
                        if this_throw_scores[0] == 10:
                            this_throw_scores.append(0)
                        this_throw_scores.append('strike')
                        print "WOW A STRIKE!"
                        self.throws_per_frame = 0
                    elif running_score_this_frame == 10:
                        this_throw_scores.append(fallen_pins_this_throw)
                        this_throw_scores.append('spare')
                        print "COOL A SPARE!"
                        self.throws_per_frame -= 1
                    else:
                        this_throw_scores.append(fallen_pins_this_throw)
                        print "Nice Shot!"
                        self.throws_per_frame -= 1
            elif hit_pins == False and self.bumpers == False:
                this_throw_scores.append(0)
                print "Oh no! A gutter ball!"
                self.throws_per_frame -= 1
            else:
                this_throw_scores.append(0)
                print "Somehow, the ball missed the pins entirely!"
                self.throws_per_frame -= 1
        return this_throw_scores

    def resetLane(self):
        """Resets the pins and balls after reach frame"""
        self.throws_per_frame = 2
        self.pins_in_lane = range(10)

    def resetBowlingGame(self):
        """Resets the bowling alley once the game is over"""
        user_continue = raw_input("That was a good game, %s!  Would you like to play again?  Please type 'Yes' or 'No'" % self.name)
        self.userGreeting()

    def showLeaderboard(self):
        """Displays the current and running score for the game"""
        pass


myGame = BowlingGame('Jessica')
myGame.userGreeting()
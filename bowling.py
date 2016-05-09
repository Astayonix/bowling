from random import choice, randint, sample

class BowlingGame(object):

    pins_in_lane = range(10)
    total_frames = range(10)
    throws_per_frame = 2
    gutter = range(2)
    bumpers = False

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
        self.showLeaderboard()

    def showLane(self):
        """Shows the current configuration of the pins in the lane"""
        if self.bumpers == True:
            print "Here is what the pins currently look line in the lane.\n\n"
            print "||}  %s %s %s %s  {||" % (self.pins_in_lane[0],self.pins_in_lane[1],self.pins_in_lane[2],self.pins_in_lane[3])
            print "||}   %s %s %s   {||" % (self.pins_in_lane[4], self.pins_in_lane[5], self.pins_in_lane[6])
            print "||}    %s %s    {||" % (self.pins_in_lane[7], self.pins_in_lane[8])
            print "||}     %s     {||\n\n" % (self.pins_in_lane[9])
        else:
            print "Here is what the pins currently look line in the lane.\n\n"
            print "{||  %s %s %s %s  ||}" % (self.pins_in_lane[0],self.pins_in_lane[1],self.pins_in_lane[2],self.pins_in_lane[3])
            print "{||   %s %s %s   ||}" % (self.pins_in_lane[4], self.pins_in_lane[5], self.pins_in_lane[6])
            print "{||    %s %s    ||}" % (self.pins_in_lane[7], self.pins_in_lane[8])
            print "{||     %s     ||}\n\n" % (self.pins_in_lane[9])

    def frameHandler(self):
        """Keeps track of the number of frames remaining in the game"""
        total_score_list = []
        for frame in self.total_frames:
            print "~~-= This is frame %s of 10 =-~~\n" % (frame+1)
            a_round = self.throwBall()
            total_score_list.append(a_round)
            self.resetLane()
        return total_score_list

    def throwBall(self):
        """Determines if the ball hits the pins in the lane or not and decrements the number of balls left to roll in the current frame"""
        running_score_this_frame = 0
        this_throw_scores = [] #[first throw, second throw, special scoring type]
        while self.throws_per_frame:
            self.showLane()
            print "O O O ...Rolling... o o o\n"
            hit_pins = choice([True, False])
            if hit_pins == True:
                print "The ball hits the pins!\n"
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
                        print "WOW A STRIKE!\n"
                        self.throws_per_frame = 0
                    elif running_score_this_frame == 10:
                        this_throw_scores.append(fallen_pins_this_throw)
                        this_throw_scores.append('spare')
                        print "COOL A SPARE!\n"
                        self.throws_per_frame -= 1
                    else:
                        this_throw_scores.append(fallen_pins_this_throw)
                        print "Nice Shot!\n"
                        self.throws_per_frame -= 1
            elif hit_pins == False and self.bumpers == False:
                bumper_choice = choice(self.gutter)
                if bumper_choice == 0:
                    this_throw_scores.append(0)
                    print "Oh no! The ball rolls into the left gutter!\n"
                else:
                    this_throw_scores.append(0)
                    print "Oh no! The ball rolls into the right gutter!\n"
                self.throws_per_frame -= 1
            else:
                this_throw_scores.append(0)
                print "Somehow, the ball missed the pins entirely!\n"
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
        the_game_list = self.frameHandler()
        total_game_tally = []
        visualization_list = []
        for each_frame in the_game_list:
            running_total = each_frame[0] + each_frame[1]
            total_game_tally.append(running_total)
            converter_list = ['X' if x == 10 else x for x in each_frame]
            if 'spare' in converter_list:
                converter_list[1] = "/"
            if 'X' in converter_list:
                i = converter_list.index(0)
                converter_list[i] = "-"
            visualization_list.append(converter_list)
        print total_game_tally
        print the_game_list
        
        print "Here is your scorecard for this game:"
        print "|--------------------------------------------------------------------|"
        print "|name: %s" % (self.name)
        print "|--------------------------------------------------------------------|"
        print "|Frame  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |"
        print "|--------------------------------------------------------------------|"
        print "|Ball 1 |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s   |" % (visualization_list[0][0], visualization_list[1][0], visualization_list[2][0], visualization_list[3][0], visualization_list[4][0], visualization_list[5][0], visualization_list[6][0], visualization_list[7][0], visualization_list[8][0], visualization_list[9][0])
        print "|--------------------------------------------------------------------|"
        print "|Ball 2 |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s   |" % (visualization_list[0][1], visualization_list[1][1], visualization_list[2][1], visualization_list[3][1], visualization_list[4][1], visualization_list[5][1], visualization_list[6][1], visualization_list[7][1], visualization_list[8][1], visualization_list[9][1])
        print "|--------------------------------------------------------------------|"
        print "|Score  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s  |  %s   |" % ()
        print "|--------------------------------------------------------------------|"

myGame = BowlingGame('Jessica')
myGame.userGreeting()
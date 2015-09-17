"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.config = []
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.config = [house for house in configuration]

    def __str__(self):
        """
        Return string representation for Mancala board
        """
        lst = list(self.config)
        lst.reverse()
        return str(lst)

    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.config[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        isWon = True
        #Start at 1 because 0 is house
        for ind in range(1,len(self.config)):
            if self.config[ind] != 0:
                isWon = False

        return isWon

    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if house_num == self.config[house_num]:
            isLegal = True
        else:
            isLegal = False

        return isLegal


    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if self.is_legal_move(house_num):
            self.config[house_num] = 0
            for house in range(house_num - 1, -1, -1):
                self.config[house] += 1
        print self.config


    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for ind in range(1, len(self.config)):
            if self.is_legal_move(ind):
                return ind
        return 0

    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic:
		After each move, move the seeds in the house closest to the store
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        legal_moves = list([])
        for ind in range(1, len(self.config)-1):
            if self.is_legal_move(ind):
                legal_moves.append(ind)
        return legal_moves


# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]

    # add more tests here
test = SolitaireMancala()
test.set_board([0, 1])
print test.choose_move()


# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())

import random

# Stores information needed to run a game of Grand Archive
class Game:
    # Constructors
    """
    Creates a Game object, which stores information needed to run a
    game of Grand Archive.
    
    @param playerOne: the first player in the game
    @param playerTwo: the second player in the game
    """
    def __init__(self, playerOne, playerTwo):
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.turnPlayer = Game.chooseFirst()
        self.spectatorList = []
    
    # Methods
        
    """
    Chooses the player who will go first. Uses 2d6 high roll.
    
    @return: the player who will go first
    """
    def chooseFirst(self):
        playerOneRoll = Game.rollDice(2, 6) # Roll 2d6
        playerTwoRoll = Game.rollDice(2, 6) # Roll 2d6
        higherRoll = Game.greaterNum(playerOneRoll, playerTwoRoll)
        
        while higherRoll == -1: # Rolls are equal, need to re-roll
            playerOneRoll = Game.rollDice(2, 6)
            playerTwoRoll = Game.rollDice(2 ,6)
            higherRoll = Game.greaterNum(playerOneRoll, playerTwoRoll)

        # Rolls are no longer equal
        if higherRoll == playerOneRoll: # Player one rolled higher
            return self.playerOne
        elif higherRoll == playerTwoRoll: # Player two rolled higher
            return self.playerTwo
            

    """
    Determines the higher of two numbers and returns it
    
    @param rollOne: the first number to compare
    @param rollTwo: the second number to compare
    @return: {rollOne} if the first roll is higher;
             {rollTwo} if the second roll is higher;
             {-1} if the rolls are equal
    """
    def greaterNum(self, rollOne, rollTwo):
        if rollOne > rollTwo:
            return rollOne
        if rollTwo > rollOne:
            return rollTwo
        else:
            return -1
    
    """
    Generates a random number based on a given number of dice with a given number of sides.
    
    @param numOfDice: the number of dice to roll
    @param numOfSides: the number of sides each die has
    """        
    def rollDice(self, numOfDice, numOfSides):
        currentRoll = 0

        for x in numOfDice:
            currentRoll += random.randint(0, numOfSides)

        return currentRoll
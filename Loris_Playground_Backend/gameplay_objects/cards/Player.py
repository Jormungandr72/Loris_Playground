# Stores player-specific data, like hands FIXME add what else the class does
class Player:
    """
    Constructs a Player object.
    
    @param username: the username of the player
    @param deck: the deck the current player is using
    @param isSpectator: {true} if the player is a spectator; {false} otherwise
    """
    def __init__(self, username, deck, isSpectator):
        self.username = username
        self.deck = deck
        self.isSpectator = isSpectator
        self.hand = []
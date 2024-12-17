# Contains information related to main deck cards.
from Card import Card

class MainCard(Card):
    # Constructors
    def __init__(self, name, types, classes, subtypes, element):
        Card.__init__(self, name, types, classes, subtypes, element)
from Card import Card

# Contains information related to main deck cards.
class MainCard(Card):
    # Constructors
    def __init__(self, name, types, classes, subtypes, element):
        Card.__init__(self, name, types, classes, subtypes, element)

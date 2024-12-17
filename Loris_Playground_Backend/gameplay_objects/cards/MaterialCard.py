# Contains information related to material deck cards.
from Card import Card

class MaterialCard(Card):
    def __init__(self, name, types, classes, subtypes, element):
        Card.__init__(self, name, types, classes, subtypes, element)

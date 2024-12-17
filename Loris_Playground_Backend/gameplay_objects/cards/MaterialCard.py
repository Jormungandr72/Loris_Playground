from Card import Card

# Contains information related to material deck cards.
class MaterialCard(Card):
    # Constructors
    def __init__(self, name, types, classes, subtypes, element):
        Card.__init__(self, name, types, classes, subtypes, element)

# Contains information universal to any card.
class Card:
    # Data fields
    _name = None
    _types = None
    _classes = None
    _subtypes = None
    _element = None

    # Constructor
    """
    Constructs a Card object.
    
    @param name: a string representing the printed name of the card
    @param types: an array of all types the card has (regalia, item, etc)
    @param classes: an array of all classes the card has (warrior, mage, etc)
    @param subtypes: an array of all subtypes the card has (ring, bauble, etc)
    @param element: an Element enum representing the element of the card
    """
    def __init__(self,  name, types, classes, subtypes, element):
        Card.setName(self, name)
        Card.setTypes(self, types)
        Card.setClasses(self, classes)
        Card.setSubtypes(self, subtypes)
        Card.setElement(self, element)
    
    #Getters
    
    """
    Returns a string representing the printed name of the card.
    
    @return: a string representing the printed name of the card
    """
    def getName(self):
        return self._name


    """
    Returns an array of all types the card has (regalia, item, etc).
    
    @return:  an array of all types the card has (regalia, item, etc)
    """
    def getTypes(self):
        return self._types
    
    """
    Returns an array of all classes the card has (warrior, mage, etc).
    
    @return: an array of all classes the card has (warrior, mage, etc)
    """
    def getClasses(self):
        return self._classes

    """
    Returns an array of all subtypes the card has (ring, bauble, etc).
        
    @return: an array of all subtypes the card has (ring, bauble, etc)
    """
    def getSubtypes(self):
        return self._subtypes

    """
    Returns an Element enum representing the element of the card
    
    @return: an Element enum representing the element of the card
    """
    def getElement(self):
        return self._element

    # Setters

    """
    Updates the string representing the printed name of the card.
    
    @param newName: the updated string representing the printed name of the card
    """
    def setName(self, newName):
        self._name = newName

    """
    Updates the array of all types the card has (regalia, item, etc).
    
    @param newTypes: The updated array of all types the card has (regalia, item, etc)
    """
    def setTypes(self, newTypes):
        self._types = newTypes
    
    """
    Updates the array of all classes the card has (warrior, mage, etc).
    
    @param newClasses: the updated array of all classes the card has (warrior, mage, etc)
    """
    def setClasses(self, newClasses):
        self._classes = newClasses

    """
    Updates the array of all subtypes the card has (ring, bauble, etc).
    
    @param newSubtpes: the updated array of all subtypes the card has (ring, bauble, etc)
    """
    def setSubtypes(self, newSubtypes):
        self._subtypes = newSubtypes

    """
    Updates the Element enum representing the element of the card.
    
    @param newElement: the updated Element enum representing the element of the card
    """
    def setElement(self, newElement):
        self._element = newElement

    # Methods
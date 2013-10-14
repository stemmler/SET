'''
SETCard implementation and helper functions for a game of SET.

For details on how this game works, see http://www.setgame.com/set

NOTE: I normally hate writing things in all caps, but
      I have done so with SET to distinguish it from a regular
      set of cards.
'''

# The corresponding name/value for each characteristic of a card.
COLORS = ['red', 'purple', 'green']
COUNTS = ['1','2','3']
SHADES =  ['solid', 'stripe', 'open']
SYMBOLS = ['diamond', 'squiggle', 'oval']

class SETCard:

    def __init__(self, repr):
        self.validate(repr)
        self._repr = repr

    def __eq__(self, card):
        return (self._repr == repr(card))

    def __int__(self):
        return int(self._repr)

    def __repr__(self):
        return self._repr

    def __str__(self):
        return "%s %s %s %s" % (self.get_color(),
                                self.get_count(),
                                self.get_shade(),
                                self.get_symbol())

    def get(self, i):
        ''' Get the characteristic at index i as an int value
        '''
        return int(self._repr[i])

    def validate(self, repr):
        ''' Helper method to validate the string passed in
            represents a valid SETCard:
            * there are exactly 4 characteristics
            * each characteristic has a value in the range [0,2]

            Raises and exception if any errors are found.
        '''
        if len(repr) != 4:
            raise Exception("ERROR: cannot create SETcard with repr %s, expecting 4 chars")
        for c in repr:
            if (int(c) < 0 or int(c) > 2):
                raise Exception("ERROR: cannot create SETcard with repr %s, each char must be in [0,1,2]")

    # Access functions to make getting a characteristic easier

    def get_color(self):
        return COLORS[self.get(0)]

    def get_count(self):
        return COUNTS[self.get(1)]

    def get_shade(self):
        return SHADES[self.get(2)]

    def get_symbol(self):
        return SYMBOLS[self.get(3)]


# The remaining are helpers to validate SETs and find the resulting card
# that would complete a set.


def getMatchingIndex(i,j):
    ''' Given two ints i,j, return the int that would
    complete the SET. 
   
    returns 
        i            if i == j
        3 - i - j    otherwise
    '''
    return i if (i == j) else (3 - i - j)

def getMatchingCard(c1, c2):
    ''' Given two cards c1, c2, return the card that
    would complete the SET.

    return SETCard s.t. isSET(c1,c2,c3) == true
    '''
    return SETCard("%d%d%d%d" % \
                   (getMatchingIndex(c1.get(0), c2.get(0)),
                    getMatchingIndex(c1.get(1), c2.get(1)),
                    getMatchingIndex(c1.get(2), c2.get(2)),
                    getMatchingIndex(c1.get(3), c2.get(3))))
    
def isSET(c1, c2, c3):
    ''' A SET consists of 3 cards on which each individual feature
    is either all the same OR all different on all three cards.

    Thus, add the int representations of each and verify that
    each digit (characteristic) is multiple of 3, implying that
    characteristic is either the same or different on each of the 
    3 cards.
    '''
    sum = int(c1) + int(c2) + int(c3)
    for c in str(sum):
        if (int(c) % 3 != 0):
            return False
    return True


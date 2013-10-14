import unittest

from card import *

'''
Simple tests for the Card class thus far. Will add more.
'''

class TestSET(unittest.TestCase):

    def test_card_create_fail(self):
        self.assertRaises(Exception, SETCard, ("111")) # too few characteristics
        self.assertRaises(Exception, SETCard, ("000111")) # too many characteristics
        self.assertRaises(Exception, SETCard, ("3333")) # outside of valid range

    def test_card_create_succeed(self):
        c = SETCard("0112")
        self.assertEqual('red',c.get_color())
        self.assertEqual('2',c.get_count())
        self.assertEqual('stripe',c.get_shade())
        self.assertEqual('oval',c.get_symbol())

    def test_get_matching_index(self):
        # all the same
        self.assertEqual(0, getMatchingIndex(0,0))
        self.assertEqual(1, getMatchingIndex(1,1))
        self.assertEqual(2, getMatchingIndex(2,2))

        # all different
        self.assertEqual(0, getMatchingIndex(2,1))
        self.assertEqual(0, getMatchingIndex(1,2))

        self.assertEqual(1, getMatchingIndex(2,0))
        self.assertEqual(1, getMatchingIndex(0,2))

        self.assertEqual(2, getMatchingIndex(0,1))
        self.assertEqual(2, getMatchingIndex(1,0))

    def test_get_matching_card(self):
        c1 = SETCard('0000')
        c2 = SETCard('0102')
        self.assertEqual(SETCard('0201'), getMatchingCard(c1,c2))
         
    def test_valid_set_simple(self):
        c1 = SETCard('0000')
        c2 = SETCard('1111')
        c3 = SETCard('2222')
        self.assertTrue(isSET(c1,c2,c3))

    def test_valid_set(self):
        c1 = SETCard('0221')
        c2 = SETCard('0121')
        c3 = SETCard('0021')
        self.assertTrue(isSET(c1,c2,c3))

    def test_invalid_set(self):
        c1 = SETCard('0000')
        c2 = SETCard('0101')
        c3 = SETCard('0021')
        self.assertFalse(isSET(c1,c2,c3))

    def test_cards_equal(self):
        self.assertTrue(SETCard("1111") == SETCard("1111"))

    def test_cards_not_equal(self):
        self.assertFalse(SETCard("0000") == SETCard("1111"))

    def test_string_repr(self):
        c = SETCard('2222')
        self.assertEqual('green 3 open oval', str(c))

        c = SETCard('1221')
        self.assertEqual('purple 3 open squiggle', str(c))

if __name__ == '__main__':
    unittest.main()

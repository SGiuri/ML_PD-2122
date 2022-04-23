import unittest
# reference: https://docs.python.org/3/library/unittest.html
import deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        # Eseguita prima di ogni test
        print("Prima del test")

    def tearDown(self):
        # Eseguita dopo ogni test
        print("Dopo ogni test")

    def test_numbero_of_cards_in_deck(self):
        print("Testing!")
        my_deck = deck.DeckOfCard()
        len(my_deck.deck)
        self.assertEqual(52, len(my_deck.deck))

    def test_numbero_of_cards_in_deck_2(self):
        print("Testing again!")
        my_deck = deck.DeckOfCard()
        len(my_deck.deck)
        self.assertEqual(52, len(my_deck.deck))


if __name__ == '__main__':
    unittest.main()

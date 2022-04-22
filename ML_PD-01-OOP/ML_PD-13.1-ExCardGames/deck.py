# deck.py
import os
import random

from matplotlib import pyplot as plt

SEMI = ["hearts", "spades", "clubs", "diamonds"]  # suits
VALORI = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "jack", "queen", "king"]  # face


class Card:

    def __init__(self, valore, seme):
        self.seme = seme
        self.valore = valore

    def __repr__(self):
        return f"Card('{self.valore}', '{self.seme}')"

    def __str__(self):
        return f"{self.valore} of {self.seme}"

    def file_name(self):
        my_file = f"{self.valore}_of_{self.seme}.png"
        my_path = os.getcwd() + "\\card_images\\"
        my_path_file = my_path + my_file
        print(my_path_file)
        return my_path_file

    def show_card(self):
        my_card_matrix = plt.imread(self.file_name())
        # print(my_card_matrix)
        plt.imshow(my_card_matrix)
        plt.axis("off")
        # ax = plt.gca()
        # ax.get_xaxis().set_visible(False)
        # ax.get_yaxis().set_visible(False)
        plt.tight_layout()
        plt.show()


class DeckOfCard:

    def __init__(self):
        self.deck = []
        for seme in SEMI:
            for valore in VALORI:
                self.deck.append(Card(valore, seme))

    def __repr__(self):
        pass

    def __str__(self):
        return f"Mazzo di {len(self.deck)} carte"

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def print_deck(self):
        print("#" * 35, end="")
        for contatore, carta in enumerate(self.deck):
            # genero una stringa che stampi il vlaore della carta in modo accettabile
            stirnga_carta = str(carta)  # meglio usare .join (vedi giu')
            # stampo la stringa:
            if contatore % 4 == 0:
                print()
            print(f"{stirnga_carta:20}", end=" ")
        print()
        print("#" * 35)

    def show_deck(self):
        fig, axes = plt.subplots(nrows=4, ncols=13)
        # plt.axis("off")
        for ax, card in zip(axes.ravel(), self.deck):
            my_card_matrix = plt.imread(card.file_name())
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            ax.imshow(my_card_matrix)
        
        plt.tight_layout()
        plt.show()

        pass

def main():
    # my_card = Card("2", "diamonds")
    # my_card.file_name()
    # my_card.show_card()
    # print(my_card)
    # print(repr(my_card))

    my_deck = DeckOfCard()
    print(my_deck)
    my_deck.print_deck()
    my_deck.shuffle_deck()
    my_deck.print_deck()
    my_deck.show_deck()


if __name__ == "__main__":
    main()

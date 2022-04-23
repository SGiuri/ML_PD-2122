# deck.py
import os
import random
import logging

from matplotlib import pyplot as plt

SEMI = ["hearts", "spades", "clubs", "diamonds"]  # suits
VALORI = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
          "jack", "queen", "king"]  # face

SEMI_SHORT = {"hearts": "♥",
              "spades": "♠",
              "clubs": "♣",
              "diamonds": "♦"}
VALORI_SHORT = {"ace": "A",
                "jack": "J",
                "queen": "Q",
                "king": "K"}
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
        # print(my_path_file)
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

    def short_name(self):
        if self.valore in VALORI_SHORT.keys():
            valore_short = VALORI_SHORT[self.valore]
        else:
            valore_short = self.valore

        return valore_short + SEMI_SHORT[self.seme]



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

    def print_deck(self, short = False):
        print("#" * 35, end="")
        for contatore, carta in enumerate(self.deck):
            # genero una stringa che stampi il vlaore della carta in modo accettabile
            if short:
                stirnga_carta = f"{carta.short_name():5}"           
            else:
                stirnga_carta = f"{str(carta):20}"  # meglio usare .join (vedi giu')
                
            # stampo la stringa:
            if contatore % 4 == 0:
                print()
            print(stirnga_carta, end=" ")
        print()
        print("#" * 35)

    def show_deck(self):
        from math import ceil
        from numpy import unravel_index
        if len(self.deck) < 13:
            my_cols = len(self.deck)
        else:
            my_cols = 13
        my_rows = ceil(len(self.deck) / my_cols)

        fig_width = my_cols * 9/13
        fig_height = my_rows * 4/4

        fig = plt.figure(figsize=(fig_width, fig_height))
        gs = fig.add_gridspec(my_rows, my_cols )

        axes = []
        matrix_dimension = (my_rows, my_cols)
        for n, card in enumerate(self.deck):

            subplot_position = unravel_index(n,matrix_dimension)
            logging.info(f"Subplot num: {subplot_position}")
            axes.append(fig.add_subplot(gs[subplot_position]))

        for ax in axes:
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

        for ax, card in zip(axes, self.deck):
            my_card_matrix = plt.imread(card.file_name())
            ax.imshow(my_card_matrix)


        # my_card_matrix = plt.imread(card.file_name())
        # fig, axes = plt.subplots(nrows=my_rows, ncols=my_cols, figsize=(fig_width,fig_height))
        # # plt.axis("off")
        #
        # for ax in axes.ravel():
        #     ax.get_xaxis().set_visible(False)
        #     ax.get_yaxis().set_visible(False)
        #
        # for ax, card in zip(axes.ravel(), self.deck):
        #     my_card_matrix = plt.imread(card.file_name())
        #
        #     ax.imshow(my_card_matrix)
        
        plt.tight_layout()
        plt.show()

        pass

    def pick_some_cards(self, n):
        some_card = []
        # TODO: Verificare che ci siano n carte nel mazzo
        for j in range(n):
            some_card.append(self.deck.pop(0))
        return LittleDeck(some_card)

class LittleDeck(DeckOfCard):

    def __init__(self, list_of_cards):
        self.deck = list_of_cards




def main():
    # my_card = Card("2", "diamonds")
    # my_card.file_name()
    # my_card.show_card()
    # print(my_card)
    # print(repr(my_card))

    logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.INFO)

    my_deck = DeckOfCard()
    my_deck.print_deck(short=True)
    my_deck.shuffle_deck()
    my_little_deck = my_deck.pick_some_cards(14)
    my_deck.print_deck(short=True)
    my_little_deck.show_deck()
    my_deck.show_deck()

if __name__ == "__main__":
    main()

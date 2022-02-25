codifica_mese = {"Gennaio": "A",
                 "Febbraio": "B",
                 "Marzo": "C",
                 "Aprile": "D",
                 "Maggio": "E",
                 "Giugno": "H",
                 "Luglio": "L",
                 "Agosto": "M",
                 "Settembre": "P",
                 "Ottobre": "R",
                 "Novembre": "S",
                 "Dicembre": "T"}

codifica_lettere_pari = {"A": 0,
                         "B": 1,
                         "C": 2,
                         "D": 3,
                         "E": 4,
                         "F": 5,
                         "G": 6,
                         "H": 7,
                         "I": 8,
                         "J": 9,
                         "K": 10,
                         "L": 11,
                         "M": 12,
                         "N": 13,
                         "O": 14,
                         "P": 15,
                         "Q": 16,
                         "R": 17,
                         "S": 18,
                         "T": 19,
                         "U": 20,
                         "V": 21,
                         "W": 22,
                         "X": 23,
                         "Y": 24,
                         "Z": 25,
                         "0": 0,
                         "1": 1,
                         "2": 2,
                         "3": 3,
                         "4": 4,
                         "5": 5,
                         "6": 6,
                         "7": 7,
                         "8": 8,
                         "9": 9}

codifica_lettere_dispari = {"A": 1,
                            "B": 0,
                            "C": 5,
                            "D": 7,
                            "E": 9,
                            "F": 13,
                            "G": 15,
                            "H": 17,
                            "I": 19,
                            "J": 21,
                            "K": 2,
                            "L": 4,
                            "M": 18,
                            "N": 20,
                            "O": 11,
                            "P": 3,
                            "Q": 6,
                            "R": 8,
                            "S": 12,
                            "T": 14,
                            "U": 16,
                            "V": 10,
                            "W": 22,
                            "X": 25,
                            "Y": 24,
                            "Z": 23,
                            "0": 1,
                            "1": 0,
                            "2": 5,
                            "3": 7,
                            "4": 9,
                            "5": 13,
                            "6": 15,
                            "7": 17,
                            "8": 19,
                            "9": 21}

# I valori numerici cos? determinati vengono addizionati e la somma si divide per il numero 26. Il carattere di controllo
# si ottiene convertendo il resto di tale divisione nel carattere alfabetico ad esso corrispondente nella sottoindicata tabella:
carattere_di_controllo = {0: "A",
                          1: "B",
                          2: "C",
                          3: "D",
                          4: "E",
                          5: "F",
                          6: "G",
                          7: "H",
                          8: "I",
                          9: "J",
                          10: "K",
                          11: "L",
                          12: "M",
                          13: "N",
                          14: "O",
                          15: "P",
                          16: "Q",
                          17: "R",
                          18: "S",
                          19: "T",
                          20: "U",
                          21: "V",
                          22: "W",
                          23: "X",
                          24: "Y",
                          25: "Z"}

'''
Elenco comuni italiani aggiornato:
https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv
'''


def verifica_CF(codice_fiscale):
    pass


print(f'"GRISMN79T16L736U"   is {verifica_CF("GRISMN79T16L736U")} -->  T')
print(f'"grismn79t16l736u"   is {verifica_CF("grismn79t16l736u")} -->  T')
print(f'"grism79T16L736U"    is {verifica_CF("grism79T16L736U")} -->  T')
print(f'"  GRISMN79T16L736U" is {verifica_CF("  GRISMN79T16L736U")} -->  T')
print(f'"grismn79t16l736u   "is {verifica_CF("grismn79t16l736u   ")} --> T')
print(f'"  grismn79T16L736U "is {verifica_CF("  grism79T16L736U  ")} --> T')
print(f'"RISMN79T16L736U"    is {verifica_CF("RISMN79T16L736U")} -->  F')
print(f'"grismn79t16l736"    is {verifica_CF("grismn79t16l736")} -->  F')
print(f'"grism79T736U"       is {verifica_CF("grism79T736U")} -->  F')
print(f'"000SMN79T16L736X"   is {verifica_CF("000SMN79T16L736X")} -->  F')
print(f'"grism079t16l736u"   is {verifica_CF("grism079t16l736u")} -->  F')
print(f'"grism79Z16L736D"    is {verifica_CF("grism79Z16L736D")} -->  F')
print(f'"GRISMN79T32L736M"   is {verifica_CF("GRISMN79T32L736M")} -->  F')
print(f'"GRISMN79T41L736I"   is {verifica_CF("GRISMN79T41L736I")} -->  T')
print(f'"GRISMN79T90L736O"   is {verifica_CF("GRISMN79T90L736O")} -->  F')
print(f'"GRISMN79T90OL736"   is {verifica_CF("GRISMN79T90OL736")} -->  F')
print(f'"GRISMN79T90Z999S"   is {verifica_CF("GRISMN79T90Z999S")} -->  F')
print(f'"GRISMNAAT90OL736"   is {verifica_CF("GRISMNAAT90OL736")} -->  F')
print(f'"GRISMN0PT90Z999S"   is {verifica_CF("GRISMN0PT90Z999S")} -->  F')
print(f'"GRISMN79TSSL736U"   is {verifica_CF("GRISMN79TSSL736U")} -->  F')
print(f'"GRISMN79TS9L736U"   is {verifica_CF("GRISMN79TS9L736U")} -->  F')

import pandas as pd

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

# I valori numerici cos? determinati vengono addizionati e la somma si divide per il numero 26.
# Il carattere di controllo
# si ottiene convertendo il resto di tale divisione nel carattere alfabetico ad esso
# corrispondente nella sottoindicata tabella:
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


def verifica_CF(codice_fiscale, verbosity=0):
    # verbosity = 0 significa che di default, la funzione non parla
    # Se quando chiamo la funzione imposto la verbosity a 1
    # stampo tutte le "print" di debug

    # Deve essere composto da 16 caratteri
    # strippo per eliminare i caratteri di spaziatura ante e post
    codice_fiscale = codice_fiscale.strip()

    if len(codice_fiscale) != 16:
        if verbosity == 1:
            print("Lunghezza Non Valida")
        return False

    # mi assicuro che i confronti sulle lettere li faccio solo con caratteri maiuscoli
    codice_fiscale = codice_fiscale.upper()

    # 0123456789012345
    # GRISMN79T16L736U
    cgnnm = codice_fiscale[:6]  # primi 6 caratteri, dallo 0 al 6 escluso

    # for carattere in cgnnm:
    #     if carattere not in string.ascii_uppercase:
    #         if verbosity:
    #             print("carattere non valido")
    #         return False

    if not cgnnm.isalpha():
        if verbosity:
            print("carattere non valido")

        return False

    anno = codice_fiscale[6:8]  # anno e; una stringa

    if not anno.isdigit():
        if verbosity:
            print("anno non valido")
        return False

    mese = codice_fiscale[8]

    if mese not in codifica_mese.values():
        if verbosity:
            print("mese non valido")
        return False

    giorno = codice_fiscale[9:11]
    if not giorno.isdigit():
        print("girono non numerico")
        return False
    if int(giorno) not in range(1, 32):
        if int(giorno) not in range(41, 72):
            if verbosity:
                print("giornoo non valido")
            return False

    lista_codici_comuni = estrai_codici_comune()
    codice_comune = codice_fiscale[11:15]
    if codice_comune not in lista_codici_comuni:
        if verbosity:
            print("Codice comune non valido")
        # Implementare verifica codici Nazione per nati all'estero
        return False

    codice_controllo = codice_fiscale[-1]

    if codice_controllo != calcola_carattere_controllo(codice_fiscale):
        if verbosity:
            print("Carattere di controllo Non Corretto")
        return False

    return True


def estrai_codici_comune():
    # Creo una stringa che contine il nome (ed eventualmente il percorso del file da leggere)
    my_file_name = "Elenco-comuni-italiani.csv"
    # COn pandas leggo il csv e creo un dataframe di tutto il file
    # Specificando la codifica (se diversa da "UTF-8") e il separatore (se diverso da ",")
    elenco_comuni_df = pd.read_csv(my_file_name, encoding="ANSI", sep=";")

    # Restituisco una lista della colonna che mi interessa
    return list(elenco_comuni_df['Codice Catastale del comune'])


def calcola_carattere_controllo(codice_fiscale, verbosity=0):
    #  012
    # "GRISMN79T16L736U"

    # Per python il carattere di indice "2" e' la "I", che per il legislatore e'
    # un carattere DISPARI

    somma = 0

    for indice, carattere in enumerate(codice_fiscale[:15], start=1):
        # enumerate restituisce oltre al carattere anche l'indice in cui il
        # carattere e' posizionato
        # Per numereare i caratteri con logica umana, definisco anche lo start a 1

        # Se il resto ( % ) della divisione per 2 e' 0 --> E' pari
        if indice % 2 == 0:
            # e' pari
            # il valore da aggiungere alla somma e' il valore associato
            # alla chiave del dizionario del carattere che sto analizzando:
            # "R" e' la prima lettera pari
            # odifica_lettere_pari["R"] e' 17
            if verbosity:
                print(indice, carattere, codifica_lettere_pari[carattere], end="-->")
            somma += codifica_lettere_pari[carattere]
            if verbosity:
                print("somma aggiornata=", somma)
        else:
            # Quindi e' dispari
            if verbosity:
                print(indice, carattere, codifica_lettere_dispari[carattere], end="-->")
            somma += codifica_lettere_dispari[carattere]
            if verbosity:
                print("somma aggiornata=", somma)

    resto_26 = somma % 26
    if verbosity:
        print(resto_26)
    carattere_previsto = carattere_di_controllo[resto_26]
    if verbosity:
        print(carattere_previsto)

    return carattere_previsto


print(f'"GRISMN79T16L736U"   is {verifica_CF("GRISMN79T16L736U")} -->  T')
print(f'"grismn79t16l736u"   is {verifica_CF("grismn79t16l736u")} -->  T')
print(f'"grismn79T16L    "    is {verifica_CF("grism79T16L736U")} -->  T')
print(f'"  GRISMN79T16L736U" is {verifica_CF("  GRISMN79T16L736U")} -->  T')
print(f'"grismn79t16l736u   "is {verifica_CF("grismn79t16l736u   ")} --> T')
print(f'"  grismn79T16L736U "is {verifica_CF("  grismn79T16L736U  ")} --> T')
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
print(f'"GRISMN79Z16L736U"   is {verifica_CF("GRISMN79Z16L736U")} -->  F')
print(f'"GRISMN79T16Z999U"   is {verifica_CF("GRISMN79T16Z999U")} -->  F')

print(f'"GRISMN79T16L736P"   is {verifica_CF("GRISMN79T16L736P")} -->  F')

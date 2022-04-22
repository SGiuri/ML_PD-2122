# MezziDiTrasporto.py

'''
MezziDiTresporto:

    - Aria:
        - Aerei
        - Elicotteri
    - Acqua
        - Navi
    - Terra:
        - Rotaia
        - Gomma

    - Propusione:
        - Motore Diesel
        - Motore Benzina
        - Motore Turbojet
        - Motore Elettrico

    - Luogo Di Partenza
    - Luogo Arrivo
    - Velocita'
    - Trasporto Pubblico
    - Trasporto Privato
    - Trasporto Merci
    - Trasporto Persone
    - Consumo Energia

Azioni che compie:
    - Parte
    - Arrivare
    - Caricare
    - Scaricare
    - Rifornisi
    '''


class MezzoDiTrasporto:

    def __init__(self, tipologia, partenza, destinazione):

        self.tipologia = tipologia
        print(f"Creato un oggetto {self.tipologia}")
        self.partenza = partenza
        self.destinazione = destinazione
        self.tassa_nazionale = 1000

    def carico_merci(self, tipologia_carico, massa_del_carico):
        print(f"Sto caricando {massa_del_carico} kg di {tipologia_carico}")

    def scarico(self):
        print(f"Scarico tutto")

    def in_partenza(self):
        print(f"Mezzo in partenza da {self.partenza}")

    def in_arrivo(self):
        print(f"Mezzo giunto a {self.destinazione}")


class Aereo(MezzoDiTrasporto):
    # Creo una classe "Aereo" che eredita tutte le funzionalita' di MezzoDiTrasposrto

    def __init__(self, partenza, destinazione):

        # self.tipologia = "Aereo"
        # self.partenza = partenza
        # self.destinazione = destinazione
        # self.tassa_nazionale = 1000
        super().__init__("Aereo", partenza, destinazione)

    def in_partenza(self):
        print(f"In decollo dall'aeroporto di {self.partenza}")

def main():

    mezzo1 = MezzoDiTrasporto("Aereo", "Venezia", "Parigi")
    mezzo1.carico_merci("Arance", 250)
    mezzo1.in_partenza()
    mezzo1.in_arrivo()
    mezzo1.scarico()
    print(mezzo1.tassa_nazionale)


    aereo1 = Aereo("Catania", "Venezia")
    aereo1.carico_merci("Limoni", 75)
    aereo1.in_partenza()
    print(aereo1.tassa_nazionale)

if __name__=='__main__':
    main()
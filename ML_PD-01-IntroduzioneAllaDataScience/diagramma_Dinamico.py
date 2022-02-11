# coding: utf-8
# Da eseguire solo se necessara istallazione della libreria, in generale alla prima esecuzione
# Il punto esclamativo sulle celle di IPython (Jupyter Nb) esegue un comando sul Terminale

# !pip install matplotlib
# !pip install numpy
# !pip install seaborn
# Le librerie standard di python che ci serviranno in questo progetto:
import random
import collections

# Le librerie dei framework specifici:
import matplotlib.pyplot as plt  # Motore grafico di python per realizzare diagrammi e fuznoni
import numpy as np  # Libreria che gestisce ad altissima efficienza gli array
import seaborn as sns  # Libreria che usa il motore grafico di MatplotLib con funzionalita' grafiche avanzate

# Tiriamo un dado "n" volte e salviamo i risultati in una lista

n_tiri = 10000
# Usiamo la list_comprehension per costruire una lista
# di numeri casuali lunga n_tiri:
# tiri = [genera un numero casuale per j che va da 0 al numero di tiri]
tiri = [random.randrange(1, 7) for j in range(n_tiri)]
# Vediamo cosa e' venuto fuori
print(f"Abbiamo una lista con {len(tiri)} elementi")
# Stampiamo anche i primi 10 elemneti:
print(f"I primi elementi di 'tiri' sono: {tiri[:10]}")
get_ipython().run_cell_magic('time', '', '\nfrequenze = collections.Counter(tiri)\n')
# Diamo un'occhiata ai risultati:
print("Da Counter di collection otteniamo:")
for val, freq in frequenze.items():
    print(f"Il numero {val} e' uscito {freq} volte")
get_ipython().run_cell_magic('time', '', '\nvalori, frequenza = np.unique(tiri, return_counts=True)\n')
# Diamo un'occhiata ai risultati:
print("Da np.unique otteniamo:")
for val, freq in zip(valori, frequenza):
    print(f"Il numero {val} e' uscito {freq} volte")
# imposto lo stile con sfondo grgietto
sns.set_style("darkgrid")

# scrivo la stringa che contiene il titolo
title = f"Diagramma delle frequenze di {len(tiri)} tiri di dado"
# creo l'oggetto axes, il digramma vero e proprio
axes = sns.barplot(x=valori, y=frequenza)

# metto su axes il titolo
axes.set_title(title, fontsize=14)

# metto le etichette sull'asse x e sull'asse y
axes.set(xlabel="Valore", ylabel="Frequenza")

# alzo il limite massimo sull'asse y per farci stare alcune informazioni sulla
axes.set_ylim(top=max(frequenza) * 1.15)

# per ciascun rettangolo (axes.patches) e ciascuna frequenza ad esso associata (frequenza_bar) nel diagramma (axes):
for bar, frequenza_bar in zip(axes.patches, frequenza):
    # recupera la posizione x del centro del rettangolo
    x_text = bar.get_x() + bar.get_width() / 2
    # bar.get_x() e' il punto in basso a sinistra del diagramma
    # a cui sommo mezza larghezza della barra
    # recupero la posizione y del testo, ovvero sopra alla barra:
    y_text = bar.get_y() + bar.get_height()
    # bar.get_y() e' il punto piu' basso del rettangolo, a cui sommo l'altezza del rettangolo stesso "bar.get_height()"

    # Il testo da scrivere sopra a ciascuna barra e' il numero di occorrenza (che ricavvo da "get_height")
    # e la percentuale (che ricavo, dal get_height, diviso per il numero dei tiri, in percentuale:
    text = f"{bar.get_height():.0f}\n{100 * bar.get_height() / len(tiri):.2f} %"

    # Stampa sul diagramma il testo (axes.text(...))
    axes.text(x_text, y_text, text,
              ha="center",  # allinea il testo al centro orizzontalmente
              va="bottom",  # allinea il testo in basso verticalmente
              fontsize=12  # imposto le dimensioni del carattere del text
              )

# mostra il diaramma a video (necessario su configurazioni non IPython)
plt.show()

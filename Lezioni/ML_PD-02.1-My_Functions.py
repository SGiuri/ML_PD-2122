"""Raccolta di funzioni utile"""

def lancio_dado(numero_facce = 6, my_seed = 42):
    """ Funzione che simula il lancio di un dado
    numero_facce: numero di facce del dado, default, 6 facce
    my_seed: seme per la generazione di numeri pseudocasuali"""
    
    from random import randint, seed
    
    seed = my_seed
    
    return randint(1, numero_facce)


def lancio_n_dadi(numero_dadi = 2):
    """ Funzione che simula il lancio di n dadi da 6"""
    
    risultato = 0
    
    for j in range(numero_dadi):
        risultato += lancio_dado() 
        
    return risultato


def lancia_n_volte_2_dadi(n=100):
    """ Simulo il lancio di due dadi per n volte
    conto il numero di volte che ottengo ciascun risultato"""
    
    r2 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    r6 = 0
    r7 = 0
    r8 = 0
    r9 = 0
    r10 = 0
    r11 = 0
    r12 = 0
    
    for lancio in range(n):
        risultato = lancio_n_dadi() # lancio due dadi da 6
        if risultato == 2:
            r2 += 1
        elif risultato == 3:
            r3 += 1
        elif risultato == 4:
            r4 += 1
        elif risultato == 5:
            r5 += 1
        elif risultato == 6:
            r6 += 1            
        elif risultato == 7:
            r7 += 1
        elif risultato == 8:
            r8 += 1
        elif risultato == 9:
            r9 += 1
        elif risultato == 10:
            r10 += 1             
        elif risultato == 11:
            r11 += 1
        elif risultato == 12:
            r12 += 1 
            
    print(r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12, sep="\n")
    






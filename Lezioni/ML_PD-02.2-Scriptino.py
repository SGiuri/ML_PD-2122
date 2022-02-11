# scriptino.py
"""Confronto tra interi utilizzando operatori di confronto"""

print("Inserisci due interi, e ti diro' in che relazione sono.")

# leggi il primo numero
number1 = int(input("Inserisci il primo intero: "))

# leggi il secondo intero
number2 = int(input("Inserisci il secondo intero: "))

if number1 == number2:
    print(f"{number1} e' uguale a {number2}")
    
if number1 != number2:
    print(f"{number1} e' diverso da {number2}")
      
if number1 > number2:
    print(f"{number1} e' maggiore di {number2}")
    
if number1 >= number2:
    print(f"{number1} e' maggiore o uguale a {number2}")

if number1 < number2:
    print(f"{number1} e' minore di {number2}")
    
if number1 <= number2:
    print(f"{number1} e' minore o uguale a {number2}")

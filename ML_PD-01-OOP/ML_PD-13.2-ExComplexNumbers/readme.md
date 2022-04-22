# Test Driven Programming
## Numeri Complessi

https://it.wikipedia.org/wiki/Numero_complesso#Operazioni_con_i_numeri_complessi


Un numero complesso e' un numero scritto nella forma `a + b * i` dove `a` e `b` sono reali e `i` soddisfa `i^2 = -1`.<br>

`a` e' detta parte reali, `b` e' detta parte immaginaria di `z`.<br>
Il _complesso coniugato_ (conjugate) del numero `a + b * i` e' il numero `a - b * i`.<br>
Il _modulo_ (absolute value) del numero complesso `z = a + b * i` e' il numero reale `|z| = sqrt(a^2 + b^2)`. <br>
Il _quadrato del valore assoluto_  `|z|^2` e' il risultato della moltiplicazione di `z` per il suo complesso coniugato.<br>

_Somma e sottrazione_ di due numeri comp!lessi si eseguono sommando e sottraendo indipendentemente la parte reale e la parte immaginaria
`(a + i * b) + (c + i * d) = (a + c) + (b + d) * i`,
`(a + i * b) - (c + i * d) = (a - c) + (b - d) * i`.

La _moltiplicazione_ consiste nell'applicazione della formual che segue:
`(a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i`.

Il _reciproco_ (reciprocal) di un numero non nullo e':
`1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i`.

_Dividere_ il numero complesso `a + i * b` per `c + i * d` restituisce:
`(a + i * b) / (c + i * d) = (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i`.

Elevare `e`, numero di eulero, alla potenza di un numero complesso, l'_esponenziale_, consiste in:<br>
`e^(a + i * b) = e^a * e^(i * b)`<br>
in cui il secondo termine e' dato dalla formula di eulero:<br>
`e^(i * b) = cos(b) + i * sin(b)`.<br>


Assumere che il linguaggio python non conosca il concetto di numero complesso e implementare le seguenti operazioni:
 - rappresentazione in forma di stringa e rappresentazione informatica del numero (`__str__` e `__repr__`)
 - addizione, sottrazione, moltiplicazione, divisione tra 2 nuemri complessi
 - coniugato, valore assoluto, esponeziale di un singolo numero complesso

See [Emulating numeric types](https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types) for help on operator overloading.


### Suggerimenti:

Vedi [Emulating numeric types](https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types) per maggiori 
informazione sull'override degli operatori.


### Exception messages
A volte puo' essere necessario sollevare un'eccezione per la gestione di eventuali errori. L'eccezione deve includere un messaggio 
significativo del problema che si dovesse presentare.
```python
raise Exception("Messaggio Significativo del problema che si e' verificato")
```

### Per eseguire i test

Da console: <br>
`pytest complex_numbers_test.py`<br>
`python -m pytest complex_numbers_test.py`

#### `pytest` options

- `-v` : abilita' la modalita' _verbose_
- `-x` : interrompe i test al primo errore
- `--ff` : esegue i test falliti alla precedente esecuzione prima di eseguire i nuovi test

Per altre opzioni: <br>
`python -m pytest -h`

## Source
Esercizio estratto da [Exercism](https://exercism.org/tracks/python/exercises/complex-numbers), riadattato e tradotto da
Simone Giuri.
Wikipedia [https://en.wikipedia.org/wiki/Complex_number](https://en.wikipedia.org/wiki/Complex_number)

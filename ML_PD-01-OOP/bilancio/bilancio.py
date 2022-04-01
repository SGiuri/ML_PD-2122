# students.py
import Decimal

class ContoCorrente:
    """Docstring descrittiva della classe. """

    def __init__(self, name, saldo):
    # inizializza un oggetto ContoCorrente
        if saldo < 0.00:
            raise ValueError("Saldo iniziale negativo NON consentito")
        self.name = name

    def daposit(self, amount):

        if amount <= 0:
            raise ValueError("L'importo del deposito deve essere positivo")

        self.saldo += amount



# bank_account.py

# importo le librerie
from decimal import Decimal

class Account:
    """ Classe che descrive un conto corrente"""
    def __init__(self, name, balance):
        """
        :param name: Nome del proprietario del conto
        :param balance: Slado iniziale del conto
        """
        self.name = name

        if balance < 0:
            raise ValueError("Saldo Negativo NON accettato")

        self.account_close = False

        self.balance = Decimal(balance)

    def print_balance(self):
        """ Stampa del nome e del saldo alla data corrente
        """
        if self.account_close:
            print(f"CC di {self.name} - Saldo = {self.balance} Euro - CONTO CHIUSO")
        else:
            print(f"CC di {self.name} - Saldo = {self.balance} Euro")

    def deposit(self, amount):
        if self.account_close:
            raise ValueError("Impossibile eseguire operazioni su un conto chiuso")
        if amount < 0:
            raise ValueError("Importo del deposito Negativo NON accettato")

        self.balance += Decimal(amount)
        print(f"Versati {Decimal(amount)} Euro")

    def withdraw(self, amount):
        if self.account_close:
            raise ValueError("Impossibile eseguire operazioni su un conto chiuso")
        if amount < 0:
            raise ValueError("Importo del prelievo Negativo NON accettato")
        if amount > self.balance:
            raise ValueError("Importo del prelievo non disponibile nel saldo")

        self.balance -= Decimal(amount)
        print(f"Prelevati {Decimal(amount)} Euro")

    def close(self):
        self.withdraw(self.balance)
        print("Conto Chiuso")

        self.account_close = True

        pass

# Sezione di scripting che viene eseguita solo se il file e' eseguito direttamente da pythone non attraverso una libreria

def main():
    conto = Account("Simone", 1000)
    conto.print_balance()

    conto.deposit(500)
    conto.print_balance()

    conto.withdraw(350)
    conto.print_balance()

    conto.close()
    conto.print_balance()
    # Se provo ad agire sul conto chiuso viene sollevata una eccezione:
    # conto.deposit(500)

if __name__ == '__main__':
    # Queste due righe di codice permettono di eseguire la funzione main solo se chiamata direttamente a partire
    # dal file che la contiene
    main()





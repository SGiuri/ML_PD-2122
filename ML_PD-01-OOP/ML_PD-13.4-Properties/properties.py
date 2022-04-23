# properties.py

class People:

    def __init__(self, name, surname):

        self.name = name.lower()
        self.surname = surname.lower()
        # self.fullname = f"{self.name.capitalize()} {self.surname.capitalize()}"

        self._fullname = self.fullname
        self._email = self.email

    @property
    def email(self):
        self._email = f"{self.name}.{self.surname}@my_mail.com"
        return self._email

    # fullname e' un attributo di sola lettura, non settabile
    # Getter, to get, va a prendersi il valore della funzione mascherata da attributo
    @property
    def fullname(self):
        self._fullname = f"{self.name.capitalize()} {self.surname.capitalize()}"
        return self._fullname

    # Setter, to set, mi permette di settare l'attributo,
    # eventualmente anche tutti gli attributi ad esso legati
    @fullname.setter
    def fullname(self, fullname):
        self.name = fullname.split()[0]
        self.surname = fullname.split()[1]
        self._fullname = self.fullname
        self._email = self.email





if __name__ == "__main__":

    people1 = People("Simone", "Giuri")
    print(people1.fullname)

    # cambio il nome:
    people1.name = "Pippo"
    print(people1.fullname)
    print(people1.email)
    print(people1.__dict__)
    people1.fullname = "Caio Sempronio"
    print(people1.email)
    print(people1.__dict__)
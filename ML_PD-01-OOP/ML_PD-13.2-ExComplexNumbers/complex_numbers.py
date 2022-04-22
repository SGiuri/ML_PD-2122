from math import e, sin, cos

class ComplexNumber:
    def __init__(self, real, imaginary):
        # 'a + b*i, Re + Im*i'
        self.real = real
        self.imaginary = imaginary
        pass

    def __repr__(self):
        # ComplexNumber(real, imaginary)
        return(f"ComplexNumber({self.real}, {self.imaginary})")

    def __str__(self):
        if self.imaginary == 0:
            return f"{self.real}"
        if self.real == 0:
            return f"{self.imaginary}i"

        if self.imaginary > 0:
            sign = "+"
        else:
            sign = "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"

    def __eq__(self, other):
        # a + b*i == c + d*i
        if isinstance(other, ComplexNumber):
            if self.real != other.real:
                return False
            if self.imaginary != other.imaginary:
                return False
            return True
        return False

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real,
                                 self.imaginary + other.imaginary)
        else:
            raise TypeError("Non posso sommare numeri complessi ad altri oggetti")


    def __mul__(self, other):
        # (a + i * b) * (c + i * d) = (a * c - b * d) + (b * c + a * d) * i

        if isinstance(other, float):
            other = ComplexNumber(other, 0)

        mul_real = self.real * other.real - self.imaginary * other.imaginary
        mul_imaginary = self.imaginary * other.real + self.real * other.imaginary

        return ComplexNumber(mul_real, mul_imaginary)

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real,
                                 self.imaginary - other.imaginary)
        else:
            raise TypeError("Non posso sommare numeri complessi ad altri oggetti")

    def __truediv__(self, other):
        # a / b = a * 1/b
        return self * (other.recyprocal())

    def __abs__(self):
        from math import sqrt
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, - self.imaginary)

    def recyprocal(self):
        # `1 / (a + i * b) = a/(a^2 + b^2) - b/(a^2 + b^2) * i`.
        a2_b2 = self.real**2 + self.imaginary**2
        return ComplexNumber(self.real/a2_b2, - self.imaginary/a2_b2)
        pass

    def exp(self):
        '''Elevare e, numero di eulero, alla potenza di un numero complesso, l'esponenziale, consiste in:
        e^(a + i * b) = e^a * e^(i * b)
        in cui il secondo termine e' dato dalla formula di eulero:
        e^(i * b) = cos(b) + i * sin(b)'''

        e_a = e**self.real # e^a
        e_ib = ComplexNumber(cos(self.imaginary), sin(self.imaginary)) #cos(b) + i * sin(b)
        return e_ib * e_a # e^a * e^(i * b)
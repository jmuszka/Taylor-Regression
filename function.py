class Polynomial:
    coefficients = []
    degree = 0
    name = ""

    def __init__(self, coefficients=[], name="p"):
        #for coeff in coefficients: 
            #if type(coeff)!=float and type(coeff)!=int: raise ValueError("Coefficients must be Real numbers")

        self.coefficients = coefficients
        self.degree = len(coefficients)
        self.name = str(name)

    def _stringify_exponent(self, n):
        _DIGITS = [
            "\N{superscript zero}",
            "\N{superscript one}",
            "\N{superscript two}",
            "\N{superscript three}",
            "\N{superscript four}",
            "\N{superscript five}",
            "\N{superscript six}",
            "\N{superscript seven}",
            "\N{superscript eight}",
            "\N{superscript nine}"
        ]

        superscripted = "".join(_DIGITS[int(d)] for d in str(n))
        return f"{superscripted}"

    def print(self):
        s = f"{self.name}(x) = "
        a = self.coefficients

        s += f"{a[0]}"        
        for i in range(1, len(a)):

            #if round(a[i], 7) == 0: s += f"{a[i]}"
            if round(a[i], 7) == 0: continue
            elif a[i] > 0: 
                if abs(round(a[i], 7)) == 1: s += f" + x{self._stringify_exponent(i)}"
                else: s += f" + {a[i]}x{self._stringify_exponent(i)}"
            elif a[i] < 0: 
                if abs(round(a[i], 7)) == 1: s += f" - x{self._stringify_exponent(i)}"
                else: s += f" - {abs(a[i])}x{self._stringify_exponent(i)}"
        
        print(s)

    def compute(self, c):
        if type(c)!=float and type(c)!=int: raise ValueError("Function input must be a Real number")

        result = 0
        a = self.coefficients
        for i in range(len(a)):
            result += a[i]*(c**i)

        return result
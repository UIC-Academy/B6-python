class Polynomial:
    def __add__(self, other):
        raise NotImplementedError
    

class QuadraticPolynomial(Polynomial):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()
    
    def __add__(self, other):
        new_polynomial = QuadraticPolynomial(
            a=self.a+other.a,
            b=self.b+other.b,
            c=self.c+other.c
        )
        return new_polynomial
        
    def __str__(self):
        return f"{self.a}x**2+{self.b}x+{self.c}"
    

class LinearPolynomial(Polynomial):
    pass


class CubicPolynomial(Polynomial):
    pass


pol1 = QuadraticPolynomial(3, 4, 3)
pol2 = QuadraticPolynomial(4, 3, 5)
res = pol1 + pol2
print(res)


"""
1, a, 3x
x+2, 3x^2+2


3x**2 + 4x + 3
4x**2 + 3x + 5
7x**2 + 7x + 8
"""
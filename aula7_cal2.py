class Calculadora:
    def __init__(self):
        pass
    def soma(self ,a,b):
        return a + b

    def subtracao(self,a,b):
        return a - b

    def multiplicacao(self,a,b):
        return a * b

    def divisao(self,a,b):
        return a / b


calculadora = Calculadora()
print(calculadora.soma(1,5))
print(calculadora.subtracao(1,6))
print(calculadora.multiplicacao(9,8))
print(calculadora.divisao(4,6))

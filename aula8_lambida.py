contador_letras = lambda lista: [len(x) for x in lista]

lista_a = ["arara", "Gato"]
print(contador_letras(lista_a))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b
}
print(type(calculadora))
soma = calculadora['soma']
print(soma(10,5))
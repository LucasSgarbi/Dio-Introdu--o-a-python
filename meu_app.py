print("oi")
a = float(input("Qual o primeiro numero ?"))
b = float(input("Qual o segundo numero ?"))

soma = a+b
subtracao = a-b
resto = a%b
divicao = a/b
multiplicacao = a*b
print("Soma = {soma} \n Subtração = {sub} \n Multiplicação = {mult} \n Divisão = {div} \n Resto = {rest}"
      .format(soma=soma, sub=subtracao , mult = multiplicacao,rest = resto , div = divicao ))
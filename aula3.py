# a= float(input("primeiro valor"))
# b = float(input("segundo valor"))
# c = float(input("Terceiro valor"))
# if a>b and a>c:
#     print("O numero : {} é o maior".format(a))
# elif b>a and b>c:
#     print('O numero :{} é o maior'.format(b))
# else:
#     print('O numero :{} é o maior'.format(c))

# a = float(input('Entre com um valor'))
# b = float(input('Entre com o segundo valor valor'))
# if a % 2 == 0 or b % 2 == 0:
#     print("Foi digitado um numero par")
# else:
#     print("Não foi digitado um numero par")

a =float(input('Informe a primeira nota '))
b =float(input('Informe a segunda nota '))
c =float(input('Informe a terceira nota '))
d =float(input('Informe a quarta nota '))
if a<=10 and b<=10 and c<=10 and d<=10 :
    print("media = {}".format((a+b+c+d)/4))
else :
    print('Algum numero imformado esta errado ')

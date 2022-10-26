lista = [1,10]
arquivo =open('teste.txt' , 'r')

try:
    texto =arquivo.read()
    divisao = 10/1
    num = lista[1]
    x=a
except ZeroDivisionError:
    print("Não é posivel divider por 0")
except ArithmeticError:
    print("Erro ao fazer uma operação aritimetica")
except IndexError:
    print('Indise invalido ')
except Exception as ex:
    print('Erro desconhecido , Erro name {}'.format(ex))
else:
    print('não ocoreu uma execão')

finally:
    print('sempre execulta')
    arquivo.close()
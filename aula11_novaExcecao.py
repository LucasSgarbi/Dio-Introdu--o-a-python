class Error (Exception):
    pass
class InputErro(Error):
    def __init__(self , message):
        self.message = message


while True:
    try:
        x = int(input('Entre com um numero de 0 a 10 : '))
        print(x)
        if x>10 :
            raise InputErro('Nota não pode ser maior que 10')
        elif x<0 :
            raise InputErro('Numero deve ser maior que 0')

        break

    except ValueError:
        print('Digite um numero')
    except InputErro as ex:
        print(ex)
from aula7_tv import TV
from aula7_cal1 import Calculadora
from aula8_contador import contador_letras,teste

if __name__ == '__main__':
    calculadora = Calculadora(5, 10)
    tv = TV()
    lista = ["arara" , "gato"]
    print(contador_letras(lista))
    tv.power()
    print(tv.ligada)
    print(calculadora.soma())
    teste()
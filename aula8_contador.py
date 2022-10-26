def contador_letras(lista):
    cont = []
    for x in lista:
        q = len(x)
        cont.append(q)
    return cont


def teste():
    print("teste")


if __name__ == '__main__':
    lista = ["gato", "tigre"]
    print(contador_letras(lista))

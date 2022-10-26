import shutil


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome, texto):
    arquivo = open(nome, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome):
    arquivo = open(nome, 'r')
    texto = arquivo.read()
    print(texto)


def media(nome):
    arquivo = open(nome, 'r')
    notas = arquivo.read()
    notas = notas.split('\n')
    lista_media = []
    for x in notas:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        med = lambda notas: sum([int(i) for i in notas]) / 4
        # print(med(lista_notas))
        lista_media.append({aluno: med(lista_notas)})
    return lista_media


def copia(nome):
    shutil.copy(nome, './copia.txt')


def move(nome):
    shutil.move(nome, '../')


if __name__ == '__main__':
    move('copia.txt')
    # copia('notas.txt')
    # medias = media('notas.txt')
    # print(medias)
    # escrever_arquivo('Primeira Linha \n')
    # aluno = '\n Abigail,10,8,9,8 '
    # atualizar_arquivo('notas.txt',aluno)
    # ler_arquivo('teste.txt')

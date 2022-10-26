lista = [1, 9, 3, 4, 5]
lista_animais = ["Cachorro", "Gato", "Tigre","Arara","Urso"]

tupla =(1,4,5,32,45) # não pode ser alterado
print(tupla)
#converter lista em tupla
tupla_animal = tuple(lista_animais)
print(tupla_animal)
#comverter tupla em lista
lista_num = list(tupla)
print(lista_num)

# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# print(lista_animais[1])
# print(sum(lista))
# print(max(lista))
# print(min(lista))
# if "Lobo" in lista_animais:
#     print("sim")
# else:
#     print("não")
#     lista_animais.append("Lobo")
# nova_lista = lista_animais*3
# print(nova_lista)
#
# lista_animais.pop(1) # sem nd tira o ultimo o numero a posição
# print(lista_animais)
#
# lista_animais.remove("Cachorro")
# print(lista_animais)
# conjunto = {1,2,3,4,5,6}
# conjunto.add(7)
# conjunto.discard(3)

conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {6, 4, 8, 2, 7}

conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)
conjunto_inter = conjunto1.intersection(conjunto2)
print(conjunto_inter)
conjunto_dif = conjunto1.difference(conjunto2)
print(conjunto_dif)
dif_simitetrica = conjunto1.symmetric_difference(conjunto2)
print(dif_simitetrica)

conjunto_a = {1,2,3,4,5}
conjunto_b = {1,2,3}
conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)
conjunto_superset =conjunto_a.issuperset(conjunto_b)
print(conjunto_superset)

lista = [1,2,3,4,5,6,2,4,4]
conjuto_lista =set(lista)
print(conjuto_lista)
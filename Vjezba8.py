def filtritaj_parne(lista):
    parni = []
    for i in lista:
        if i%2==0:
            parni.append(i)
    return parni

lista = [1, 2,3,4,5,6,7,8,9,10]
print(filtritaj_parne(lista))


# ili

def filtriraj_parne_brojeve(lista):
    # Kreira novu listu koja sadrži samo parne brojeve
    return [broj for broj in lista if broj % 2 == 0]

# Primjer korištenja funkcije
originalna_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = filtriraj_parne_brojeve(originalna_lista)
print(nova_lista)
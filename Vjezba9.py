def ukloni_duplikate(lista):
    skup = set()
    nova_lista = []

    for broj in lista:
        if broj not in skup:
            nova_lista.append(broj)
            skup.add(broj)
    return nova_lista

originalna_lista = [1,2,3,4,5,1,2,3,4,5]
nova_lista = ukloni_duplikate(originalna_lista)
print(nova_lista)

#ili kraće

def ukloni_duplikate(lista):
    unikatni = []
    for broj in lista:
        if broj not in unikatni: 
            unikatni.append(broj)
    return unikatni

lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(ukloni_duplikate(lista))
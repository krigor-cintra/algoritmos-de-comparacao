
def bubble_sorts(lista,i):
    auxiliar : int
    a= i+1
    if a == (len(lista)):
        return lista

    elif (lista[i] > lista[a]):
        auxiliar = lista[a]
        lista[a] = lista[i]
        lista[i] = auxiliar
        return bubble_sorts(lista, a)
    else:
        return bubble_sorts(lista,a)






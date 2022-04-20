#bubble sort
from listas import l2


def bubble_sort(lista):
    tamanho=len(lista)
    auxiliar: int
    for i in range (tamanho-1):
        a=i+1
        if(a==tamanho+1):
            a=i
            if (lista[i] >=lista[a]):
                auxiliar = lista[i]
                lista[i] = lista[a]
                lista[i] = auxiliar
        elif (lista[i]>=lista[a]):
            auxiliar=lista[i]
            lista[i]=lista[a]
            lista[a]=auxiliar





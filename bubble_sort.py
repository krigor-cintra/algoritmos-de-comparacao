from time import time
import time


def bubble_sort(lista):
    timei = time.time()
    time.sleep(0.0000000000001)
    tamanho=len(lista)
    auxiliar: int
    for e in range (tamanho):
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
    timef = time.time()
    timeend= timef-timei
    return lista,timeend

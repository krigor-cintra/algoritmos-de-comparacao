from time import time
import time
def selection_sort(list):
    timei = time.time()
    time.sleep(0.0000000000001)
    tamanho = len(list)
    auxiliar: int
    for i in range(tamanho):
        for j in range(tamanho):
            if (list[i] < list[j]):
                auxiliar = list[i]
                list[i] = list[j]
                list[j] = auxiliar
    timef = time.time()
    timeend = timef - timei

    return list,timeend
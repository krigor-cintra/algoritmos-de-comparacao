def insertion_sort(list):
    tamanho=len(list)
    auxiliar: int
    j=1
    for i in range(tamanho):
        if (list[i]<list[j]):
            auxiliar = list[i]
            list[i]= list[j]
            list[j] = auxiliar
            j=j+1

    return list

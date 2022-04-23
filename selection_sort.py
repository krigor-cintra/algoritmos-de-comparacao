def selection_sort(list):
    tamanho = len(list)
    auxiliar: int
    for i in range(tamanho):
        for j in range(tamanho):
            if (list[i] < list[j]):
                auxiliar = list[i]
                list[i] = list[j]
                list[j] = auxiliar

    return list
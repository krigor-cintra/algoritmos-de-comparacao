def shell_sort_ajudante(lista, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > temp:
                lista[j] = lista[j - intervalo]
                j -= intervalo

            lista[j] = temp
        intervalo //= 2
def shell_sort(lista):
    n1=len(lista)
    shell_sort_ajudante(lista,n1)
    return lista


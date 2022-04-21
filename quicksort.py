
def partition(lista, low, high):
  pivot = lista[high]
  i = low - 1
  for j in range(low, high):
    if lista[j] <= pivot:
      i = i + 1
      (lista[i], lista[j]) = (lista[j], lista[i])
  (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
  return i + 1


def quick_sort_ajudante(lista, low, high):
  if low < high:

    pi = partition(lista, low, high)

    quick_sort_ajudante(lista, low, pi - 1)
    quick_sort_ajudante(lista, pi + 1, high)


def quick_sort(lista):
  quick_sort_ajudante(lista, 0, len(lista) - 1)


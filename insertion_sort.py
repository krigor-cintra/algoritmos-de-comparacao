def insertion_sort(list):

    for step in range(1, len(list)):
        key = list[step]
        j = step - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key

    return list

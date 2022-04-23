from time import time
import time
def insertion_sort(list):
    timei = time.time()
    time.sleep(0.0000000000001)
    for step in range(1, len(list)):
        key = list[step]
        j = step - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    timef = time.time()
    timeend = timef - timei

    return list,timeend

def insertionSort(array):
    n = len(array)
    for i in range(n):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value


myList = [-3, 53, 54, 26, 93, 17, 77, 31, 44, 55, 8978, 521, 254, 654, 32, 41, 5, 54, 56, 20]
insertionSort(myList)
print(myList)

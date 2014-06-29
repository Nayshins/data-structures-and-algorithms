def insertionSort(list):
    for index in range(1,len(list)):
        currentValue = list[index]
        position = index

        while position > 0 and list[position-1] > currentValue:
            list[position] = list[position-1]
            position = position-1

        list[position] = currentValue
        
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
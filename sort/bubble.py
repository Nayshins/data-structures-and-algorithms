def bubbleSort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

test = [55,2,8,7,14,13,1,19]

bubbleSort(test)
print(test)
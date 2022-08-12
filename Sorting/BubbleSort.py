def bubbleSort(array):
    sorted_arr = False
    counter=0
    while not sorted_arr:
        sorted_arr = True
        for j in range(len(array)-counter-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                sorted_arr = False
        counter+=1
    return array

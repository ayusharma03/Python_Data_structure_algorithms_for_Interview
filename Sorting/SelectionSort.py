def selectionSort(array):
    # Write your code here.
    curr_index = 0
    while curr_index < len(array)-1:
        min_index = curr_index
        for i in range(curr_index+1,len(array)):
            if array[min_index]>array[i]:
                min_index=i
        swap(curr_index,min_index,array)
        curr_index+=1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]
            

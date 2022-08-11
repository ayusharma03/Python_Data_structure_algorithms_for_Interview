# Best : O(nlog(n)) time | O(log(n)) space
# Average : O(nlog(n)) time | O(log(n)) space
# Worst : O(n^2)) time | O(log(n)) space

def quickSort(array):
    # Write your code here.
	quickSortHelper(array, 0, len(array) - 1)
	return array
		
def quickSortHelper(array, low, high):
	print("Quicksorthelper")
	if low >= high:
		return
	pivot = array[low]
	left = low + 1
	right = high
	while right >= left:
		if array[left] > pivot and array[right] < pivot:
			swap(array, left, right)
		if array[left] <= pivot:
			left += 1
		if array[right] >= pivot:
			right -= 1
	swap(array, low, right)
	leftSubArrayIsSmaller = right - 1 - low < high - (right + 1)
	if leftSubArrayIsSmaller:
		quickSortHelper(array, low, right - 1)
		quickSortHelper(array, right + 1, high)
	else:
		quickSortHelper(array, right + 1, high)
		quickSortHelper(array, low, right - 1)

def swap(array, one, two):
	array[one], array[two] = array[two], array[one]
  
 

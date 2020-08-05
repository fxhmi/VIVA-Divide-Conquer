def heapify(arr, n, i):										# n = size of heap, i = root
	largest = i 											# Initialize largest as root
	l = 2*i+1	 											# left = 2*i + 1
	r = 2*i+2												# right = 2*i + 2

	if l < n and arr[i] < arr[l]:							# if left child exists && greater than root, make it largest
		largest = l

	if r < n and arr[largest] < arr[r]:						# if right child exists && greater than root/left child, make it largest
		largest = r

	if largest != i:										# if largest not initial root, swap root with largest
		arr[i],arr[largest] = arr[largest],arr[i]
		heapify(arr, n, largest)							# repeat heapify

def heapSort(arr):
	n = len(arr)											# n = size of heap

	for i in range(n, -1, -1):								# build max heap with heapify
		heapify(arr, n, i)

	for i in range(n-1, 0, -1):								# sorting the array by extracting the sorted nodes
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)



arr = [84, 23, 62, 44, 16, 30, 95, 51]
print ("Initial array :")
for i in range(len(arr)):
	print ("%d" %arr[i], end = '')
	if i < len(arr)-1:
		print (",", end = '')


heapSort(arr)
print (" ")
print ("Sorted array :")
for i in range(len(arr)):
	print ("%d" %arr[i], end = '')
	if i < len(arr)-1:
		print (",", end = '')

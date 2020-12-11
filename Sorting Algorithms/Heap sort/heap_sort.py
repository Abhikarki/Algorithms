# Random unsorted array.
A = [5, 4, 8, 2, 9, 5, 7, 3, 6, 8, 1]
# length of the list.
n = len(A)

def main():
    print("Unsorted List: ")
    for i in range(n):
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(A[i], end = ' ')
    # To print new line.
    print()
    # Call the build_max_heap function.
    build_max_heap()
    # Once the heap is built the size of heap is equal to that of array.
    heap_size = n
    # The deletion function will actually sort the array.
    deletion(heap_size)

    print("Sorted List: ")
    for i in range(n):
        print(A[i], end = ' ')

def build_max_heap():
    i = int((n -1) / 2)
    while i >= 0:
        heapify(i, n)
        i -= 1
    return    

def heapify(i, heap_size):
    # set the parent element to largest for comparision.
    largest = A[i]
    large_index = i
    # Index of the left child.
    left = (2 * i) + 1
    # Check if the left child is within the heap_size.
    if left < heap_size and A[left] > largest:
        largest = A[left]
        large_index = left

    # Index of the right child.
    right = (2 * i) + 2
    # Check if the left child is within the heap_size.
    if right < heap_size and A[right] > largest:
        largest = A[right]
        large_index = right

    # swap the parent with larger child(if it exists) to maintain max heap property.
    if large_index != i:
        A[large_index] = A[i]
        A[i] = largest
        # If swapping takes place, Call the heapify function with the swapped position.
        heapify(large_index, heap_size)

    return    

def deletion(heap_size):
    # The following loop continuously brings the current largest element of the heap 
    # to the end of the array , maintains the heap (heapify),
    # and also decreases the size of heap by 1 in each iteration.     
    while heap_size > 1:
        # Swap the root of the heap with last element of the heap.
        root = A[0]
        A[0] = A[heap_size - 1]
        A[heap_size - 1] = root
        # Decrease the size of the heap by 1.
        heap_size -= 1
        # The current root element violates the max heap property. So,        
        # call the heapify function with index of the root and heap_size.
        heapify(0, heap_size)
    return    

# Call main function to execute the code.
main()       

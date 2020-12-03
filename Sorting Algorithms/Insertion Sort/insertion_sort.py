# Random unsorted array.
A = [5, 4, 8, 2, 9, 5, 7, 3, 6, 8, 1]

# length of the list.
length = len(A)

def main():
    print("Unsorted List: ")
    for i in range(length):
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(A[i], end = ' ')
    # To print new line.
    print()
    # Call insertion_sort function.
    insertion_sort()
    
    print("Sorted List: ")
    for i in range(length):
        print(A[i], end = ' ')     

def insertion_sort(): 
    for i in range(1, length):
        k = i
        j = i - 1
        # Following loop inserts the element into the sorted part of the list.
        while j >= 0:
            if A[k] < A[j]:
                # store the value in temp variable.
                temp = A[k]
                A[k] = A[j]
                A[j] = temp
                j -= 1
                # k should be decreased to locate the new position of the element.
                k -= 1  
            else:
                # break out of the while loop.
                break  

# Call the main function.
main()

   
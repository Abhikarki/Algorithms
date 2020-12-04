# Random unsorted array.
A = [5, 4, 8, 2, 9, 5, 7, 3, 6, 8, 1]

# Length of the list.
length = len(A)

def main():
    print("Unsorted List: ")
    for i in range(length):
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(A[i], end = ' ')
    # To print new line.
    print()
    # Call selection_sort function.
    selection_sort()
    
    print("Sorted List: ")
    for i in range(length):
        print(A[i], end = ' ') 


def selection_sort():
    for i in range(length):
        # Set the ith element to min value for comparision with rest of the elements.
        # min_value is updated only if there is a smaller number in remaining unsorted list.
        min_value = A[i]
        # t is the index of the current mimimum value.
        t = i 
        for j in range(i+1, length):
            # Check for a smaller number from (i+1) to last position.
            if A[j] < min_value:
                # update the minimum value.
                min_value = A[j]
                # update t.
                t = j
        # Update the ith element only if it is not in the correct position.        
        if t != i:        
            A[t] = A[i]
            # update the ith element to minimum value.
            A[i] = min_value

#Call the main function.
main()                   
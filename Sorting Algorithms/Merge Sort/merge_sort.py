# Random unsorted array.
A = [5, 4, 8, 2, 9, 5, 7, 3, 6, 8, 1]

def main():
    # Length of the list.
    length = len(A)
    start = 0
    print("Unsorted List: ")
    for i in range(length):
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(A[i], end = ' ')
    # To print new line.
    print()
    # Call merge_sort function.
    merge_sort(start, length - 1)
    
    print("Sorted List: ")
    for i in range(length):
        print(A[i], end = ' ')     

def merge_sort(start, end):
    if start < end:
        T = (end + start) / 2
        # Converting T to an integer in case it is a decimal number.
        mid = int(T)
        # Recursion.
        # Call merge_sort function for right and left halves.
        merge_sort(start, mid)
        merge_sort(mid + 1, end)     

        # Merge the elements by sorting.
        # Call the merge function.
        merge(start, mid, end)
    
    # Return if start >= end i.e. if start index >= end index.   
    else:
        return

def merge(start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
     
    # Creating temporary lists of sizes n1 and n2.
    # Values are initialized to 0.
    temp1 = [0] * n1
    temp2 = [0] * n2

    # Copy the elements to temporary lists for sorting.
    for i in range(0, n1):
        temp1[i] = A[start + i]

    for j in range(0, n2):   
        temp2[j] = A[mid + 1 + j]

    g = 0
    h = 0
    # Start index.
    s = start
    # To sort and merge the temporary lists.
    # Also known as 2-way merge or a binary merge.
    while g < n1 and h < n2:
        if temp1[g] <= temp2[h]:
            A[s] = temp1[g]
            g += 1
        else:
            A[s] = temp2[h]
            h += 1
        s += 1

    # To copy the remaining elements from temp1 array (if any).
    while g < n1:
        A[s] = temp1[g]
        g += 1
        s += 1

    # To copy the remaining elements from temp2 array (if any).
    while h < n2:
        A[s] = temp2[h]
        h += 1
        s += 1   

# Call the main function.
main()
# HASHING WITH CHAINING
# Class of student.
class student:
    def __init__(self, k, name):
        # student's rank.
        self.rank = k
        # student's name
        # Assume that all students have unique names.
        self.name = name
        # pointer to next object in chain.
        self.next = None
        # pointer to previous object in chain.
        self.prev = None

# hash function
def h(name):
    # get the acii value of the first letter
    temp = ord(name[0])
    return temp % 10


# function to insert elements into hash table.
def insert(k, name, arr):
    # temp variable
    tmp = student(k, name)
    hash_value = h(name)
    # set the next pointer of the new object to that of the array index.
    tmp.next = arr[hash_value].next
    tmp1 = tmp.next
    if tmp1 is not None:
        tmp1.prev = tmp
    # set the array index to point at object.
    arr[hash_value].next = tmp
    # set the prev pointer of the object to array index.
    tmp.prev = arr[hash_value]
    

def search(name, arr):
    # Compute the hash value.
    hash_value = h(name)
    temp = arr[hash_value].next
    # search for the student in the chain(linked list).
    while temp is not None:
        tmp_str = temp.name
        if tmp_str == name:
            print(name + "'s rank is " + str(temp.rank))
            return
        temp = temp.next
    
    print(name + " not found")    
                

def main():
    # Initialize a array(hash table).
    arr = [student(0, "x")] * 10
    # insertion
    insert(5, "bill", arr)
    insert(2, "john", arr)
    insert(11, "emily", arr)
    insert(5, "mike", arr)
    insert(4, "peter", arr)
    insert(5, "lois", arr)
    insert(22, "brian", arr)
    insert(9, "michael", arr)
    insert(5, "pam", arr)
    insert(20, "jim", arr)
    insert(9, "kelly", arr)
    insert(5, "dwight", arr)
    insert(5, "mark", arr)
    insert(6, "craig", arr)
    insert(12, "stanley", arr)
    insert(7, "angela", arr)
    insert(9, "martha", arr)
    insert(3, "brad", arr)
    insert(4, "leo", arr)
    insert(5, "jennifer", arr)
    insert(3, "miley", arr)
    insert(6, "anne", arr)

    search("anne", arr)
    search("Bob", arr)
    search("jim", arr)


# Call the main function to execute the code.
main()        
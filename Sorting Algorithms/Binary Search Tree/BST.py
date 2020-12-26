# MAKING AN UNBALANCED BINARY SEARCH TREE.

class BST_Node:
    def __init__(self, k):
        self.key = k
        # pointers to left and right child nodes respectively.
        self.left = None
        self.right = None
        # pointer to parent node.
        self.parent = None
        

# Recursive function for insertion of elements.
def insertion(node, k):
    # create a new node.
    if node == None:
        return BST_Node(k)
    if node.key > k:
        node.left = insertion(node.left, k)
        # Set the parent of the node.
        tmp_node = node.left
        tmp_node.parent = node
    else:
        node.right = insertion(node.right, k)
        # Set the parent of the node.
        tmp_node = node.right
        tmp_node.parent = node

    return node

# Function to find the next larger key in the tree.
# Also known as inorder successor.
def find_next_larger(node, k):
    # if the node doesnot have any right child.
    if node.right is None:
        # Continue comparision upto root element.
        while node is not None:
            if node.key > k:
               return node
            # Update node to be its parent node.
            node = node.parent
        # return none if successor is not found.
        return None

    # Else, if the node has right child node or subtree.
    else:
        # Update the node to be its right child.
        node = node.right
        # Continue searching towards left.
        while node.left != None:
            node = node.left
        return node       

# Function to search for a key in the tree.
def search(node, k):
    # Loop to search for the key.
    while node != None:
        if node.key == k:
            # return the node if key is found.
            return node
        # search in the left subtree.
        elif node.key > k:
            node = node.left
        # search in the left subtree.
        else:
            node = node.right
    # return None if the key is not found.
    return None            

# Function to find the inorder predecessor.
def find_predecessor(node, k):
    # if the node doesnot have any left child.
    if node.left is None:
        # Continue comparision upto root element.
        while node != None:
            if node.key < k:
                return node
            # Update node to be its parent node.
            node = node.parent
        # return none if predecessor is not found.
        return None

    # if the node has left child node or subtree.
    else:
        # Update the node to be its left child.
        node = node.left
        # Continue searching towards right.
        while node.right != None:
            node = node.right
        return node    

# To delete a node(while maintaining the property of binary search tree.)
def delete(root, k):
    # If the tree is empty.
    if root is None:
        return root

    # search the node to be deleted
    if root.key > k:
        root.left = delete(root.left, k)
    elif root.key < k:
        root.right = delete(root.right, k)
    # If the node is found.
    else:
        # If the node has only one child or is a leaf node.
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp       
        
        # If the node has two children,
        # place the key of the inorder successor node in the node to be deleted.
        else:
            tmp = find_next_larger(root, k)
            # Update the key of the node to its successor.
            root.key = tmp.key           
            # Delete the inorder successor
            root.right = delete(root.right, tmp.key)

    return root
    
            
# Recursive function for inorder traversal i.e the sorted order.
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # print the key.
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(str(root.key) + " ", end = ' ')

        # Traverse right
        inorder(root.right)   

# To search and print the inorder successor of a key.
def find_successor(root, k):
    # first search for the key.
    tmp1 = search(root, k)
    if tmp1 is None:
        print("key " + str(k) + " not found.")
    else:
        # pointer to the node with next larger key.
        tmp2 = find_next_larger(tmp1, tmp1.key)
        # if the pointer is none, there is no larger element.
        if tmp2 is None:
            print(str(k) + " is the largest element")
        # Else, print the next larger key.
        else:
            print("successor of "+ str(k) + " is " + str(tmp2.key))



def main():
    root = None
    # Insert nodes to the binary search tree.
    root = insertion(root, 42)
    root = insertion(root, 13)
    root = insertion(root, 40)
    root = insertion(root, 26)
    root = insertion(root, 23)
    root = insertion(root, 18)
    root = insertion(root, 2)
    root = insertion(root, 6)
    root = insertion(root, 20)
    root = insertion(root, 32)
    root = insertion(root, 39)
    root = insertion(root, 60)
    root = insertion(root, 62)
    root = insertion(root, 68)
    root = insertion(root, 17)
    root = insertion(root, 61)
    root = insertion(root, 70)
    root = insertion(root, 35)
    # After the insertions, the tree looks like:
    #                 42
    #               /    \
    #             13      60
    #           /    \       \
    #          2      40      62
    #           \     /      /  \
    #            6   26     61   68
    #               /  \           \
    #             23    32         70
    #            /        \
    #           18        39
    #          /  \      /
    #         17   20   35


    # To print the sorted list.
    inorder(root)
    
    # delete 26.
    delete(root, 26)
    print()

    # To print the new sorted list.
    inorder(root)
    print()

    # finding the next larger key to 40, 70, and 55.
    find_successor(root, 40)
    find_successor(root, 70)
    find_successor(root, 55)
                    
# Call the main function to execute the code.
main()

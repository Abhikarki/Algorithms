# MAKING A BALANCED BINARY SEARCH TREE.

class AVL_Node:
    def __init__(self, k):
        self.key = k
        # pointers to left and right child nodes respectively.
        self.left = None
        self.right = None
        # pointer to parent node.
        self.parent = None
        # height = longest path from node down to a leaf.      
        self.height = 0
        
        # Height of the left subtree(initialize to -1 for easy arithmetic)
        self.left_height = -1
        # Height of the right subtree.
        self.right_height = -1
        # balance_factor = height of left subtree - height of right subtree.
        self.balance_factor = 0

    # Method for computing the height and balance_factor.
    def compute(self):        
        left = self.left
        if left is not None:
            self.left_height = left.height
        else:
            self.left_height = -1

        right = self.right
        if right is not None:
            self.right_height = right.height
        else:
            self.right_height = -1

        # compute the balance_factor
        self.balance_factor = self.left_height - self.right_height
        # compute the height.
        self.height = 1 + max(self.left_height, self.right_height)



# Recursive function for insertion of elements.
def insertion(node, k):
    # create a new node.
    if node == None:
        return AVL_Node(k)
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

    # update the height and balance_factor of the node.
    node.compute()
    # Call the rotate function if the subtree is not balanced.
    if abs(node.balance_factor) > 1:
        return rotate(node)

    return node



# To delete a node(while maintaining the property of the AVL tree.)
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
        else:
            # find the inorder successor of the node to be deleted.
            tmp = find_next_larger(root, k)
            # Update the key of the node to its successor.
            root.key = tmp.key           
            # Delete the inorder successor
            root.right = delete(root.right, tmp.key)

    # Update the height and balance_factor of the node.
    root.compute()
    # Call the rotate function if the subtree is not balanced.
    if abs(root.balance_factor) > 1:
        return rotate(root)

    return root



# Function for rotation of the nodes as per the conditions.
def rotate(node):
    # If the node is heavier on the left side.
    if node.balance_factor > 1:
        first = node.left   
        # There can be two cases.
        # Case 1: The node's left child is also left heavy.
        if first.balance_factor >= 0:
            return right_rotate(node, first)
            
        # Case 2: The node's left child is right heavy.
        else:
            # The right child of the node's left child.           
            second = first.right
            # Two rotations are needed
            # first rotate the node's child and grandchild.
            # Then it becomes similar to case 1.
            first = left_rotate(first, second)
            return right_rotate(node, first)
            
    # If the node is heavier on the right side.
    else:
        first = node.right
        # There can be two cases.
        # Case 1: The node's right child is also right heavy.
        if first.balance_factor <= -1:
            return left_rotate(node, first)
        # Case 2: The node's right child is left heavy.
        else:
            # The left child of the node's right child.
            second = first.left
            # Two rotations are needed
            # first rotate the node's child and grandchild.
            # Then it becomes similar to case 1.
            first = right_rotate(first, second)
            return left_rotate(node, first)        

# Function for the right rotation.
def right_rotate(node1, node2):
    # Arrange the pointers between the nodes for the rotation.
    # Note: The order should be followed, otherwise we may lose
    # the node(i.e. the address of the node.)
    node1.left = node2.right
    node2.right = node1
    node2.parent = node1.parent
    tmp = node1.parent
    # if node1 is root, tmp = None. So, check the condition
    if tmp is not None:
        if tmp.left == node1:
            tmp.left = node2
        else:
            tmp.right = node2
    node1.parent = node2
    
    # Update the balance_factor and height of the nodes.
    # Note: The following order should be maintained i.e
    # first, update the child and then the parent as below:
    node1.compute()
    node2.compute()
    # return node2
    return node2        


# Function for the left rotation.
def left_rotate(node1, node2):
    # Arrange the pointers between the nodes for the rotation.
    # Note: The order should be followed, otherwise we may lose
    # the node(i.e. the address of the node.)
    node1.right = node2.left
    node2.left = node1
    node2.parent = node1.parent
    tmp = node1.parent
    # if node1 is root, tmp = None. So, check the condition
    if tmp is not None:
        if tmp.left == node1:
            tmp.left = node2
        else:
            tmp.right = node2
    node1.parent = node2
    
    # Update the balance_factor and height of the nodes.
    # Note: The following order should be maintained i.e
    # first, update the child and then the parent as below:
    node1.compute()
    node2.compute()
    # return node2
    return node2          


# Function to find the node with next larger key in the tree.
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


# Function to find the node with inorder predecessor.
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


# To search and print the inorder successor of a key.
def find_successor(root, k):
    # first search for the key.
    tmp1 = search(root, k)
    # if key not found.
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


# Recursive function for inorder traversal i.e the sorted order.
def inorder(root):
    if root is not None:
        # Move to left
        inorder(root.left)

        # print the key.
        # Changes the end parameter in print() from
        # default value '\n' to ' '.
        print(str(root.key) + " ", end = ' ')

        # Move to right
        inorder(root.right)   


def main():
    root = None

    root = insertion(root, 42)
    root = insertion(root, 13)            
    root = insertion(root, 50)        
    root = insertion(root, 5)            
    root = insertion(root, 7)        
    root = insertion(root, 8)        
    root = insertion(root, 60)        
    root = insertion(root, 70)        
    root = insertion(root, 3)        
    root = insertion(root, 9)        
    root = insertion(root, 10)        
    root = insertion(root, 80)        
    #After insertions, the tree looks like:
    #                  13
    #                /    \
    #               7      50
    #             /  \    /  \
    #            5    9  42   70
    #           /    / \     /  \
    #          3    8   10  60   80
     

    inorder(root)
    print()
    # delete a node.
    delete(root, 50)
    inorder(root)
    print()

    print("The root is " + str(root.key))
    print("The height of the tree is " + str(root.height))

    find_successor(root, 10)

# Call the main function to execute the code
main()    

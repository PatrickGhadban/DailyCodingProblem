'''
* Difficulty: Medium
* Asked by: LinkedIn
* Problem: Determine whether a tree is a valid binary search tree.
    A binary search tree is a tree with two children, left and right, and satisfies
    the constraint that the key in the left child must be less than or equal to the
    root and the key in the right child must be greater than or equal to the root.


Time Taken: 25mins
RunTime: O(n)
Space Complexity: O(1)

Description: Base Case - starting at the root, check if the node is empty.
             Set an upper and a lower bound to represent a spectrum of values that the child node(s) can fall into.
             Start with values that essentially equate to +/- infinity, and that will be replaced with the respected
             values of that childs parent node.
'''
class node:
    def __init__(self, value = None):
        self.value = value
        self.right = None
        self.left = None

def is_BST(tree):
    MIN = -999999999999999
    MAX = 9999999999999999
    return _is_BST(tree, MIN, MAX)

def _is_BST(cur_node, lower_bound, upper_bound):
    #Base case - Empty Tree
    if cur_node == None:
        return True
    if cur_node.value < lower_bound or cur_node.value > upper_bound:
        return False
    else:
        return _is_BST(cur_node.left, lower_bound, cur_node.value ) and _is_BST(cur_node.right, cur_node.value, upper_bound)



def main():
    tree1 = node(10)
    tree1.left = node(0)
    tree1.left.left = node(-1)
    tree1.left.right = node(21)
    tree1.right = node(25)
    tree1.right.left = node(16)
    tree1.right.right = node(32)

    tree2 = node(10)
    tree2.left = node(-10)
    tree2.left.left = node(-20)
    tree2.left.right = node(0)
    tree2.right = node(19)
    tree2.right.left = node(17)


    print(is_BST(tree1)) #Should return False
    print(is_BST(tree2)) #Should return True

if __name__ == "__main__":
    main()

'''
* Difficulty: Easy
* Asked by: Google
* Problem: Given the root of a binary tree, return a deepest node.
    For example, in the following tree, return d.
         a
        /\
       b  c
      /
     d

Time Taken: 1hr
RunTime: O(N)
Space Complexity: O(1)

Description:
'''

class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in tree.")

    def print_tree(self):
        if self.root == None:
            print ("Tree is empty")
        else:
            self._print_tree(self.root)
    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(cur_node.value)
            self._print_tree(cur_node.right)

    def deepest_node(self, root):
        if root == None:
            return 0
        else:
            left = self.deepest_node(root.left)
            right = self.deepest_node(root.right)
            return max(left, right) + 1

def main():
    tree = BST()
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.print_tree()
    print ("DEPTH: ", tree.deepest_node(tree.root))

if __name__ == "__main__":
    main()

#Importing a tree node module
from tree_node_module import tree_node

#Creating a binary tree
class binary_tree:

    def __init__(self, root):
        self.root = tree_node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, " ")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, " ")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, " ")
            
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
        
    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


#               1
#           /       \
#          2         3
#         / \       /  \
#        5   8     4    7
# preorder - 1-2-5-8-3-4-7-
# inorder  - 5-2-8-1-4-3-7-

tree = binary_tree(1)
tree.root.right = tree_node(3)
tree.root.right.left = tree_node(4)
tree.root.right.right = tree_node(7)
tree.root.left = tree_node(2)
tree.root.left.left = tree_node(5)
tree.root.left.right = tree_node(8)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("None"))

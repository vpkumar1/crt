class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, root):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(data, root.left)
        elif data > root.data:
            root.right = self.insert(data, root.right)
        return root

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

    def search_in_bst(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        if key < root.data:
            return self.search_in_bst(root.left, key)
        else:
            return self.search_in_bst(root.right, key)

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
bst_tree = BST()
root = None
root = bst_tree.insert(20, root)
root = bst_tree.insert(10, root)
root = bst_tree.insert(900, root)
root = bst_tree.insert(5, root)
root = bst_tree.insert(15, root)

print("Inorder Traversal:")
bst_tree.inorder_traversal(root)
print("\n")

key = 888800
if bst_tree.search_in_bst(root, key):
    print(f"Element {key} is present in the tree")
else:
    print(f"Element {key} is not present in the tree")
tree_height = bst_tree.height(root)
print(f"\nHeight of the BST: {tree_height}")

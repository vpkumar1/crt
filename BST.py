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
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")
bst_tree = BST()
bst_tree.root = bst_tree.insert(20, bst_tree.root)
bst_tree.root = bst_tree.insert(30, bst_tree.root)
bst_tree.root = bst_tree.insert(900, bst_tree.root)
print("Inorder Traversal:")
bst_tree.inorder_traversal(bst_tree.root)

print("\nPreorder Traversal:")
bst_tree.preorder_traversal(bst_tree.root)

print("\nPostorder Traversal:")
bst_tree.postorder_traversal(bst_tree.root)

class node:
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    def inorder_traversal(self,node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)
    def preorder_traversal(self,node):
        if node:
            self.preorder_traversal(node.left)
            print(node.data)
            self.preorder_traversal(node.right)
    def postorder_traversal(self,node):
        if node:
            self.postorder_traversal(node.left)
            print(node.data)
            self.postorder_traversal(node.right)
    def sum_of_nodes(self,node):
        if node is none:
            return 0
        return node.data+self.sum_of_nodes(node.left)+self.sum_of_nodes(node.right)
tree=node()
tree.data=1
tree.left=node()
tree.left.data=2
tree.right=node()
tree.right.data=3
tree.left.right=node()
tree.left.right.data=4
tree.right.left=node()
tree.right.left.data=5
tree.inorder_traversal(node=tree)
tree.preorder_traversal(node=tree)
tree.postorder_traversal(node=tree)
print(tree.data)
print(tree.left.data)
print(tree.right.data)
print(tree.left.right.data)
print(tree.right.left.data)
print(tree.sum_of_nodes(node=tree.right))
print(tree.sum_of_nodes(node=tree.left))
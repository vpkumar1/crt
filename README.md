BST:

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

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, root, value):
        if root is None:
            return False
        if value == root.data:
            return True
        elif value < root.data:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

bst_tree = BST()
bst_tree.root = bst_tree.insert(20, bst_tree.root)
bst_tree.root = bst_tree.insert(10, bst_tree.root)
bst_tree.root = bst_tree.insert(900, bst_tree.root)
print("Inorder traversal:")
bst_tree.inorder_traversal(bst_tree.root)
print("\nPreorder traversal:")
bst_tree.preorder_traversal(bst_tree.root)
print("\nPostorder traversal:")
bst_tree.postorder_traversal(bst_tree.root)
print("\nSearch results:")
print("10 found?", bst_tree.search(10)) 
print("100 found?", bst_tree.search(100)) 
print("\nHeight of tree:", bst_tree.height(bst_tree.root))
OUTPUT:
Inorder traversal:
10 20 900 
Preorder traversal:
20 10 900 
Postorder traversal:
10 900 20 
Search results:
10 found? True
100 found? False

Height of tree: 2
1.	You are given an integer array of size N, representing jars of chocolates. Three
students A, B, and C respectively, will pick chocolates one by one from each chocolate
jar, till the jar is empty, and then repeat the same with the rest of the jars. Your task
is to fine and return an integer value representing the total number of chocolates that
student A will have, after all the chocolates have been picked from all the jars.
Note: Once a jar is done A will start taking the chocolates from the new jar.
Input Format :
input1: An integer array representing the quantity of chocolates in each jar.
input2: An integer value N representing the number of jars.
Output Format:
Return an integer value representing the total number of chocolates that student A
will have, after all the chocolates are picked.
Example:
Input:
10 20 30
3
Output:
21
2.	
Max is having a dog . he want  to find the age of the dog 
with respect to the age of human.
he came to know that , the age of the
dog is mesured with respect to human  has a formula to proceed. 
example: 1 year of life span of dog is same as
seveen years of  life span  of human being
Now , calculate the age of MAX dog.

3.	Max is planning to take part in a Diwali contest at a Diwali Party that will begin at 8
PM and will run until midnight (12 AM) i.e., for 4 hours. He also needs to travel to the
party venue within this time which takes him P minutes. The contest comprises
of N problems that are arranged in order of difficulty, with problem 1 being the
simplest and problem N being the most difficult. Max is aware that he will require 5*i
minutes to solve the ith problem.
Your task is help Max find and return an integer value, representing the number of
problems Max can solve and reach the party venue within the given time frame of 4
hours.
Note: Max will leave his home at exactly 8 PM to reach the party venue.
Input Format:
input1: An integer value N, representing the total number of problems.
input2: An integer value P, Representing the time to travel in minutes from his home
to the party venue.
4.	Count the no of spaces in a string
5.	Move hyphes
PROGRAME:
s = "hello-----world"
count_hyphen=s.count('-')
new_str='-'*count_hyphen + s.replace('-',' ')
print(new_str)
print("count of extra spaces")
count_spaces=new_str.count(' ')
new_str=new_str.replace('    ', ' ')
print(new_str)
OUTPUT:
-----hello     world
count of extra spaces
-----hello  world


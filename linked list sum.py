# linked list pass sum
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None     #starting point of linked list
        
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node   # move the node
            
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")
        
    def add_ll(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
        
            
ll=LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.display()
print("sum of elements in linked list is ")
ans=ll.add_ll()
print(ans)
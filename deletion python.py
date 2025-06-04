class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
    def delete_start(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def delete_position(self, pos):
        if pos == 1:
            self.delete_start()
        else:
            temp = self.head
            for i in range(pos - 2):
                if temp is None or temp.next is None:
                    print("Position out of bounds")
                    return
                temp = temp.next
            if temp.next is None:
                print("Position out of bounds")
                return
            temp.next = temp.next.next
ll = LinkedList()
ll.insert_at_beginning(100)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_beginning(40)
ll.insert_at_beginning(50)
ll.display()
ll.delete_start()
print("After deleting at start:")
ll.display()
ll.delete_end()
print("After deleting at end:")
ll.display()
ll.delete_position(5)
print("After deleting at position 5:")
ll.display()


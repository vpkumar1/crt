class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return f"Found {key} at position {position}"
            current = current.next
            position += 1
        return f"{key} not found in the list"
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.search(20))
print(ll.search(40))  

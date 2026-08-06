class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    
    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_last(self, data):
        if self.head is None:
            self.head = self.insert_at_begin(data)

        new_node = Node(data)
        current = self.head
        while (current.next):
            if current is None:
                return
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        if position == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        current = self.head
        for i in range(position - 1):
            if current.next is None:
                return
            current = current.next
        
        if current is None:
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next is not None:
            current.next.prev = new_node
        current.next = new_node
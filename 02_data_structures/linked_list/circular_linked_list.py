class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head 
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head 
        result = []

        while cur:
            result.append(cur.data)
            cur = cur.next
            if cur == self.head:
                break
        print(result)
    
    def remove(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head: # reach the end of list
                cur = cur.next
            if self.head == self.head.next: # check if only one node is present
                self.head = None
            else:
                cur.next = self.head.next 
                self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count
    
    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_clist = CircularLinkedList()
        while cur.next != self.head:
            split_clist.append(cur.data)
            cur = cur.next
        split_clist.append(cur.data)

        self.print_list()
        split_clist.print_list()

    def remove_node(self, node):
        if self.head:
            if self.head == node:
                cur = self.head 
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next 
                    self.head = self.head.next
            else:
                cur = self.head 
                prev = None
                while cur.next != self.head:
                    prev = cur 
                    cur = cur.next 
                    if cur == node:
                        prev.next = cur.next
                        cur = cur.next
        
    def josephus_circle(self, step):
        cur = self.head
        length = len(self)

        while length > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
                print("KILL " + str(cur.data))
                self.remove_node(cur) 
                cur = cur.next
                length -= 1

    def is_circular_linked_list(self, input_list):
        if input_list.head:
            cur = input_list.head
            while cur.next:
                cur = cur.next
                if cur.next == input_list.head:
                    return True
            return False
        else:
            return False

# --------------- #
print("#-------------------------------------#")
print("append and prepend")
cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("remove a node by key")
cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.print_list()
print("removing A and C")
cllist.remove("A")
cllist.remove("C")
cllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("split a circular list into two circular lists")
# A -> B -> C -> D -> ...
# A -> B -> ... and C -> D -> ...

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.print_list()
cllist.split_list()

# --------------- #
print("#-------------------------------------#")
print("josephus circle")
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

cllist.print_list()
cllist.josephus_circle(2)
cllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("check if its a circular linked list")
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

print(cllist.is_circular_linked_list(cllist))

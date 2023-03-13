class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        cur = self.head
        result = []
        while cur:
            result.append(cur.data)
            cur = cur.next
        print(result)

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key: # only one element in the list
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
                return
            cur = cur.next
                
    def add_before_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
                return
            cur = cur.next
    
    def delete(self, key):
        cur = self.head
        while cur:
            # key matches to head/first node
            if cur.data == key and cur == self.head:
                # Case 1 - key matches to head/first node, and there is just one node in list
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # Case 2 - key matches to head/first node, and there are more nodes in list
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return
            # key matches to other than head/first node
            elif cur.data == key:
                # Case 3 - somewhere between the list
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # Case 4 - last node of the list
                else:
                    prev = cur.prev
                    prev.next = None 
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
# --------------- #
print("#-------------------------------------#")
print("append and prepend")
dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("add after/before node")
dllist = DoublyLinkedList()

dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)
dllist.print_list()

print("add 6 after key 3")
dllist.add_after_node(3,6)
dllist.print_list()

print("add 9 before key 4")
dllist.add_before_node(4,9)
dllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("delete a node")
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()

print("delete 1,6 and 4")
dllist.delete(1)
dllist.delete(6)
dllist.delete(4)
dllist.print_list()
print("delete 3")
dllist.delete(3)
dllist.print_list()

# --------------- #
print("#-------------------------------------#")
print("reverse a list")
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
dllist.reverse()
dllist.print_list()
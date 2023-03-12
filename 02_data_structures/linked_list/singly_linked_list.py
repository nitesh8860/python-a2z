"""
------------------------ Singly Linked List -------------------------
"""
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = Node()

	def append(self, data):
		new_node = Node(data)
		cur = self.head
		while cur.next != None:
			cur = cur.next
		cur.next = new_node

	def length(self):
		cur = self.head
		count = 0
		while cur.next != None:
			count += 1
			cur = cur.next
		return count

	def length_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.length_recursive(node.next)

	def display(self):
		elements = []
		cur = self.head
		while cur.next != None:
			cur = cur.next
			elements.append(cur.data)
		return elements

	def get(self, index):
		if index >= self.length():
			return "ERROR : index out of range!"
		idx = 0
		cur = self.head
		while cur.next != None:
			cur = cur.next
			if idx == index:
				return cur.data
			idx += 1

	def delete_by_index(self, index):
		if index >= self.length():
			return "ERROR : index out of range!"
		idx = 0
		cur = self.head
		while cur.next != None:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = cur.next
				return "Node Deleted"
			idx += 1
	
	def delete_by_value(self, key):
		cur_node = self.head
		if cur_node and cur_node.data == key:
			self.head = cur_node.next 
			cur_node = None
			return
		
		prev = None
		while cur_node and cur_node != key:
			prev = cur_node
			cur_node = cur_node.next

		if cur_node is None:
			return
		
		prev.next = cur_node.next
		cur_node = None

	def insert(self, index, value):
		if index > self.length():
			return "ERROR : index out of range!"
		elif index == self.length():
			self.append(value)
			return "Node Added"
		new_node = Node(value)
		idx = 0
		cur = self.head
		while cur.next != None:
			last_node = cur
			cur = cur.next
			if idx == index:
				last_node.next = new_node
				new_node.next = cur
				return "Node Added"
			idx += 1

	def swap_nodes(self, key_1, key_2):

		if key_1 == key_2:
			return 

		prev_1 = None 
		curr_1 = self.head 
		while curr_1 and curr_1.data != key_1:
			prev_1 = curr_1 
			curr_1 = curr_1.next

		prev_2 = None 
		curr_2 = self.head 
		while curr_2 and curr_2.data != key_2:
			prev_2 = curr_2 
			curr_2 = curr_2.next

		if not curr_1 or not curr_2:
			return 

		if prev_1:
			prev_1.next = curr_2
		else:
			self.head = curr_2

		if prev_2:
			prev_2.next = curr_1
		else:
			self.head = curr_1

		curr_1.next, curr_2.next = curr_2.next, curr_1.next

	def reverse_iterative(self): # ABCD
		prev = None # None
		cur = self.head # A
		while cur: # A B C D
			nxt = cur.next # B C D None
			cur.next = prev  # None A B C
			prev = cur # A B C D
			cur = nxt # B C D None
		self.head = prev # A B C D

	def reverse_recursive(self):
		def _reverse_recursive(cur, prev):
			if not cur:
				return prev
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt 
			return _reverse_recursive(cur, prev)
		
		self.head = _reverse_recursive(cur=self.head, prev=None)

	def merge_sorted(self, llist):
		p = self.head
		q = llist.head
		s = None

		if not p:
			return q
		if not q:
			return p
		
		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s

		while p and q:
			if p.data <= q.data:
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next
		
		if not p:
			s.next = q
		if not q:
			s.next = p

		self.head = new_head
		return self.head

	def remove_duplicates(self):
		cur = self.head
		prev = None
		dup_values = dict()

		while cur:
			if cur.data in dup_values:
				prev.next = cur.next
				cur = None
			else:
				dup_values[cur.data] = 1
				prev = cur
			cur = prev.next

llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print("Original List")
print(llist.display())


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
print(llist.display())

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
print(llist.display())

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
print(llist.display())

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
print(llist.display())


llist = SinglyLinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
print(llist.display())
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
print(llist.display())

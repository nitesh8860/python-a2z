class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# for level order traversal
class Queue(object):
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items) 
    
    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.size() == 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

# for reverse level order traversal
class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class BinaryTree(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """ Root -> Left -> Right """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """ Left -> Root -> Right """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """ Left -> Right -> Root """
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
        
    def levelorder_print(self, start):
        if start is None:
            return
        
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)


        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()

            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal
    
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size
    
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

# --------------- #
print("#-------------------------------------#")
print("pre/in/post order traversal")
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print("postorder")
print(tree.print_tree("postorder"))

# --------------- #
print("#-------------------------------------#")
print("level order traversal")
print(tree.print_tree("levelorder"))
print("reverse level order traversal")
print(tree.print_tree("reverse_levelorder"))

# --------------- #
print("#-------------------------------------#")
print("height of the tree")
print(tree.height(tree.root))
print("size of the tree - iterative")
print(tree.size())
print("size of the tree - recursive")
print(tree._size(tree.root))
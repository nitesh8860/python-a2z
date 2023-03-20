class Node(object):
    def __init__(self, value) -> None:
        self.data        = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root) -> None:
        self.root = Node(root)

    def insert(self, val):
        self.insert_helper(self.root, val)

    def insert_helper(self, current, val):
        if current.data < val:
            if current.right:
                self.insert_helper(current.right, val)
            else:
                current.right = Node(val)
        else:
            if current.left:
                self.insert_helper(current.left, val)
            else:
                current.left = Node(val)

    def search(self, val):
        return self.search_helper(self.root, val)
    
    def search_helper(self, current, val):
        if current:
            if current.data == val:
                return True
            elif current.data < val:
                return self.search_helper(current.right, val)
            else:
                return self.search_helper(current.left, val)
    
    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root) 
            
print("search")
bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))

print("is binary search tree ?")
bst = BST(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

tree = BST(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
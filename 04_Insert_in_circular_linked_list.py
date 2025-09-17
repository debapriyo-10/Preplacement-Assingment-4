class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror(root):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

mirror(root)
inorder(root)
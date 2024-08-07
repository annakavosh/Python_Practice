## Preorder Traversal
## Root - Left - Right

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# recursive
def Preorder(root):
    if root is None:
        return
    print(root.value, end  = " ")
    Preorder(root.left)
    Preorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    Preorder(root)
    print()
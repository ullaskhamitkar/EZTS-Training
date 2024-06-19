class node:
    def __init__(self,data):
        self.value = data
        self.left = None
        self.right = None

    def preorder(root):
        if root == None:
            return
        
        print(root.value)
        node.preorder(root.left)
        node.preorder(root.right)

if __name__ == "__main__":
    root = node(1)

    root.left = node(2)
    root.right = node(3)

    root.left.left = node(4)
    root.left.right = node(5)
    
    root.right.left = node(6)
    root.right.right = node(7)

    node.preorder(root)
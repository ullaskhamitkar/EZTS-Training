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

    def levelOrder(root):
        Q = [root]
        Q.append(None)

        while len(Q)>0:
            current = Q.pop(0)

            if current == None:
                if len(Q)==0:
                    break
                else:
                    print()
                    Q.append(None)

            else:
                print(current.value, end=' ')
                if current.left != None:
                    Q.append(current.left)
                if current.right != None:
                    Q.append(current.right)

if __name__ == "__main__":
    root = node(1)

    root.left = node(2)
    root.right = node(3)

    root.left.left = node(4)
    root.left.right = node(5)
    
    root.right.left = node(6)
    root.right.right = node(7)

    root.left.right.left = node(8)
    root.left.right.right = node(9)
    root.right.right.right = node(10)

    root.left.right.left.left = node(11)
    root.left.right.left.right = node(12)

node.levelOrder(root)
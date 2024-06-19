from levelOrder import node
class node_data:
    def __init__(self,Node,HKey):
        self.node = Node
        self.hkey = HKey
    
def topview(root):
    temp = node_data(root,0)
    Q=[temp]
    Q.append(None) 

    Key_dict = {}

    while len(Q)!=0:
        current = Q.pop(0)

        if current == None:
            if len(Q)==0:
                break
            else:
                Q.append(None)

        else:
            if current.hkey not in Key_dict.keys():
                Key_dict[current.hkey] = current.node.value
            
            if current.left != None:
                temp = node_data(current.left,current.hkey-1)
                Q.append(temp)
            if current.right != None:
                temp = node_data(current.right,current.hkey+1)                
                Q.append(temp)
        for i in sorted(Key_dict):
            print(Key_dict[i])

        print(Key_dict)

    topview(root)
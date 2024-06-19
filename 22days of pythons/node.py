class node:
    def __init__(self,data):
        self.value = data
        self.next = None
        
head = tail=node(10)

tail.next = node(20)
tail = tail.next

tail.next = node(30)
tail = tail.next

tail.next = node(40)
tail = tail.next

print (head)
print (tail)
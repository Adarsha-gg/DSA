class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head = None) -> None:
        self.head = Node()

    def append(self,node):
        current = self.head
        if current:
           while current.next:
                current = current.next
           current.next = node       
        else:
            self.head = node

    def delete(self, value):
        
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None
               
               
               



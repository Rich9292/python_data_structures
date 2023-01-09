from . import node as nd

class single_linked_list:
    # does not hold nodes themselves, just reference to head node
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head == None

    def add(self,node_value):
        temp = nd.node(node_value)
        temp.set_next(self.head)
        self.head = temp

    def print(self):
        if self.is_empty():
            print("list is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.get_value())
                curr = curr.get_next()

    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.get_next()
        return count

    def search(self,value):
        curr = self.head
        while curr != None:
            if curr.get_value() == value:
                return True
            curr = curr.get_next()
        return False

    def remove(self,value):
        curr = self.head
        prev = None
        while curr != None:
            if curr.get_value() == value:
                break
            prev = curr
            curr = curr.get_next()
        if curr == None:
            print("value not in list")
        elif prev == None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    def append(self,value):
        temp = nd.node(value)
        curr = self.head
        prev = None
        while curr != None:
            prev = curr
            curr = curr.get_next()
        if prev == None:
            self.head = temp
        else:
            prev.set_next(temp)
                

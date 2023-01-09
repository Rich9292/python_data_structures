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
            print(curr.get_value())
            while curr.get_next() != None:
                curr = curr.get_next()
                print(curr.get_value())

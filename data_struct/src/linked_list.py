from . import node as nd

class single_linked_list:
    # does not hold nodes themselves, just reference to head node
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head == None    

    def prepend(self,node_value):
        # O(1)
        temp = nd.node(node_value)
        temp.set_next(self.head)
        self.head = temp

    def print(self):
        # O(n)
        if self.is_empty():
            print("list is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.get_value())
                curr = curr.get_next()

    def size(self):
        # O(n)
        curr = self.head
        count = 0
        while curr != None:
            count += 1
            curr = curr.get_next()
        return count

    def search(self,value):
        # O(n)
        curr = self.head
        while curr != None:
            if curr.get_value() == value:
                return True
            curr = curr.get_next()
        return False

    def remove(self,value):
        # O(n)
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
        # O(n)
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
                
class double_linked_list:
    def __init__(self,head=None):
        self.head = head

    def insert_after(self,index,value):
        if (self.head == None):
            self.prepend(value)
            return
        
        temp = nd.double_node(value)
        curr = self.head
        count = 0
        while curr != None:
            if count == index:
                break
            count += 1
            curr = curr.get_next()

        if curr == None:
            print("index not in list")
        elif curr.get_next() == None:
            self.append(value)
        else:
            temp.set_next(curr.get_next())
            curr.get_next().set_prev(temp)
            curr.set_next(temp)
            temp.set_prev(curr)
        

    def append(self,value):
        temp = nd.double_node(value)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.get_next() != None:
                curr = curr.get_next()
            curr.set_next(temp)
            temp.set_prev(curr)


    def prepend(self,value):
        temp = nd.double_node(value)
        if self.head == None:
            self.head = temp
        else:
            temp.set_next(self.head)
            self.head.set_prev(temp)
            self.head = temp


    def print(self):
        if self.head == None:
            print("list is empty")
        else:
            curr = self.head
            while curr != None:
                print(curr.get_value())
                curr = curr.get_next()

    def size(self):
        # TODO
        pass

    def is_empty(self):
        return self.head == None

    def search(self,value):
        # TODO
        pass
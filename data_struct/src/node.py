class node:
    # node for a single linked list

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value

class double_node:
    # node for double linked list
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def get_value(self):
        return self.value


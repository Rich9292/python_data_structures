class node:
    # node for a linked list

    def __init__(self, value):
        self.value = value
        self.next_node = None

    def set_next(self, next_node):
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def get_value(self):
        return self.value


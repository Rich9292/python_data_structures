# # can use this file to run data structures without installing package


# create some nodes
import data_struct.src.node as nd
some_node = nd.node(1,2)
print(some_node.get_value())
print(some_node.get_next())

# create a single linked list
import data_struct.src.single_linked_list as sll
some_sll = sll.single_linked_list()
# # can use this file to run data structures without installing package


# create a node
import data_struct.src.node as nd
my_node =  nd.node("data for my node")

# create a single linked list and add some nodes
import data_struct.src.linked_list as ll
my_sll = ll.single_linked_list()
my_sll.add('node1')
my_sll.add('node2')
my_sll.add('node3')
my_sll.print()

test = 0
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

# print the list, check size, search for node
my_sll.print()
print(my_sll.size())
print(my_sll.search('node1'))

# remove node
my_sll.remove('node3')
my_sll.print()

# append node
my_sll.append('node3')
my_sll.print()

test = 0
# can use this file to run data structures without installing package


# create a node
import data_struct.src.node as nd
my_node =  nd.node("data for my node")

# create a single linked list and add some nodes
import data_struct.src.linked_list as ll
my_sll = ll.single_linked_list()
my_sll.prepend('node1')
my_sll.prepend('node2')
my_sll.prepend('node3')
#my_sll.print()

# create a double linked list and add some nodes
my_dll = ll.double_linked_list()
my_dll.insert_after(0,'node1')
my_dll.insert_after(0,'node2')
my_dll.insert_after(1,'node3')

my_dll.insert_after(1,'node2.5')
my_dll.insert_after(3,'node4')
my_dll.insert_after(0,'node0')

my_dll.prepend('prepended node')

my_dll.append('appended node')

my_dll.print()
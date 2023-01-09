# import os, sys
# parent = os.path.abspath('..')
# sys.path.insert(1, parent)
# import src.node as nd
# uncomment above if you want to run this file by itself (need to run from curr dir)

from ..src import linked_list as ll

def test_answer():

    # test adding nodes to beginning works
    my_sll = ll.single_linked_list()
    my_sll.add('node1')
    my_sll.add('node2')
    my_sll.add('node3')
    temp = my_sll.head
    assert temp.get_value() == "node3"
    temp = temp.get_next()
    assert temp.get_value() == "node2"
    temp = temp.get_next()
    assert temp.get_value() == "node1"
    temp = temp.get_next()
    assert temp == None

    # test size
    assert my_sll.size() == 3

    # test search
    assert my_sll.search('node1') == True
    assert my_sll.search('node5') == False

    # test remove node
    assert my_sll.search('node3') == True
    my_sll.remove('node3')
    assert my_sll.search('node3') == False

    # test append node
    assert my_sll.search('node3') == False
    my_sll.append('node3')
    assert my_sll.search('node3') == True
    
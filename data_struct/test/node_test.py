from ..src import node as nd

def tester():

    a = nd.node(1)
    b = nd.node(2)
    a.set_next(b)
    print("Here is value of node a: ",a.get_value())
    print("Here is value of node b: ",b.get_value())
    print("Here is value of next node from a: ",a.get_next().get_value())
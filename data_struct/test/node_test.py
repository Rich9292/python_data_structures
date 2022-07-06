from ..src import node as nd

def test_answer():

    a = nd.node(1)
    b = nd.node(2)
    a.set_next(b)

    assert a.get_value()            == 1
    assert b.get_value()            == 2
    assert a.get_next().get_value() == 2

from pystarter.slist import stack


def test_list():
    lst = stack((1, 2, 3, 4, 5, 6))

    for i in reversed(range(1, 7)):
        assert lst.pop() == i

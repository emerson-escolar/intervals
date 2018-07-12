import intervals
import math

def test_interval_definition():
    assert intervals.check_interval((1,2), 3)
    assert intervals.check_interval((0,2), 3)

    # same:
    assert intervals.check_interval((0,2), math.inf)
    assert intervals.check_interval((0,2))

    assert not intervals.check_interval((1,3),3)
    assert not intervals.check_interval((3,2))
    assert not intervals.check_interval((-1,2))



def test_nonzero_morphisms():
    assert intervals.has_nonzero_morphism((2,2), (2,2))

    assert intervals.has_nonzero_morphism((5,10), (5,10))

    assert intervals.has_nonzero_morphism((6,10), (5,10))
    assert not intervals.has_nonzero_morphism((5,10), (6,10))

    assert intervals.has_nonzero_morphism((5,10), (5,9))
    assert not intervals.has_nonzero_morphism((5,9), (5,10))

    assert intervals.has_nonzero_morphism((6,10), (5,9))
    assert not intervals.has_nonzero_morphism((5,9), (6,10))

    assert not intervals.has_nonzero_morphism((5,6), (7,10))
    assert not intervals.has_nonzero_morphism((7,10), (5,6))


def test_zigzag_morphisms_on_monodirectional():
    N = 10
    orient = "f" * (N-1)

    for dom in intervals.intervals_iter(N):
        for codom in intervals.intervals_iter(N):
            zz_algo = intervals.has_nonzero_zigzag_morphism(dom, codom,orient)
            standard_algo = intervals.has_nonzero_morphism(dom, codom)
            print(dom, "->", codom)
            assert zz_algo == standard_algo

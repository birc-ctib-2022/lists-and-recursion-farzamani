# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

import lists
from lists import L

def test_contains():
    assert lists.contains(L(1, L(2, L(3, None))), 4) == False
    assert lists.contains(L(1, L(2, L(3, None))), 2) == True

def test_drop():
    x = L(1, L(2, L(3, L(4, None))))
    assert lists.drop(x, 0) == L(1, L(2, L(3, L(4, None))))
    assert lists.drop(x, 1) == L(2, L(3, L(4, None)))
    assert lists.drop(x, 3) == L(4, None)

def test_keep():
    x = L(1, L(2, L(3, L(4, None))))
    assert lists.keep(x, 0) == None
    assert lists.keep(x, 1) == L(1, None)
    assert lists.keep(x, 3) == L(1, L(2, L(3, None)))

def test_concat():
    x = L(1, L(2, L(3, None)))
    y = L(4, L(5, None))
    assert lists.concat(x, y) == L(1, L(2, L(3, L(4, L(5, None)))))
    assert lists.concat(y, x) == L(4, L(5, L(1, L(2, L(3, None)))))

def test_append():
    assert 1 == 1

def test_rev():
    assert 1 == 1
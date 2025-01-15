import pytest
from MyTestApp import pthon

def test_true(self):
    tst = pthon()
    assert tst.stuffToTest()

def test_false(self):
    tst = pthon()
    assert not tst.stuffToTest()

# To invoke the pytest framework and run all tests
if __name__ == "__main__":
  pytest.main()
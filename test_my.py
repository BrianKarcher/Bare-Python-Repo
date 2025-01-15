import pytest
from pthon import pthon

def test_true():
    tst = pthon()
    assert tst.stuffToTest()

# To invoke the pytest framework and run all tests
if __name__ == "__main__":
  pytest.main()
import pytest
from src.MyTestApp import MyTestApp

def test_true():
    tst = MyTestApp()
    assert tst.stuffToTest() == "Hello World"

# To invoke the pytest framework and run all tests
if __name__ == "__main__":
  pytest.main()
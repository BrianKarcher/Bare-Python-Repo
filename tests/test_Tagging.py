import pytest
from src.Tagging import Tagging, File

def test_tagging():
    tagging = Tagging()
    tagging.add_file('coll1', File('file1', 100))
    tagging.add_file('coll1', File('file2', 500))
    tagging.add_file('coll1', File('file3', 800))
    tagging.add_file('coll2', File('file4', 80000))
    tagging.add_file('coll2', File('file5', 80000))
    tagging.add_file('coll3', File('file6', 800000))
    res = tagging.top_n(2)
    assert len(res) == 2
    assert 'coll2' in res
    assert 'coll3' in res

# To invoke the pytest framework and run all tests
if __name__ == "__main__":
  pytest.main()
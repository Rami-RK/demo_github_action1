# test_1.py
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from script import addition
def test_add():
    subj = addition(2, 3)
    assert subj == 5

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


from script import addition

def test_data_type():
    subj=addition(2,3)
    assert isinstance(subj,int)
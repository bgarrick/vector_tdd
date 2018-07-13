from src.vector import Vector

def test_make_vector():
    v = Vector ([1,2,3])
    assert len(v.nums) == 3
    

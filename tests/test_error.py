import numpy as np
from core.error import compute_error

def test_zero_error():
    a = np.array([[0,0,0],[1,1,1]])
    b = np.array([[0,0,0],[1,1,1]])

    err = compute_error(a, b)
    assert (err == 0).all()

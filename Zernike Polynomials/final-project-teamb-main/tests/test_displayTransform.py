import numpy as np
from displayTransform import displayTransform
from Transform import Transform
import pytest

#some model data
class fakeData():
    def __init__(self, data, system):
        self.data = data
        self.system = system

#test for zernikes        
def test_zernike():   
    data = [np.array([1, 2]), np.array([0.5, 0.9])]
    transform = fakeData(data, 'Zernike')
    
    x_expected, y_expected = displayTransform.polar_to_cartesian(data[0], data[1])
    data_expected = np.stack([x_expected, y_expected])
    
    displayTransform.display(transform, 'intensity')
    x, y = displayTransform.polar_to_cartesian(data[0], data[1])
    np.testing.assert_array_equal(x, x_expected)
    np.testing.assert_array_equal(y, y_expected)
    np.testing.assert_array_equal(np.stack([x, y]), data_expected)
    

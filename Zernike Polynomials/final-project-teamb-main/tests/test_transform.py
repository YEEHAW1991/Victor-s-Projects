import numpy as np
import pytest
from Transform import Transform


    
parametrize_vars = "system,coeffs,coeffs_names,indices,indices_names"
parametrize_struct = [
    ("Zernike", "1, 2, 3", "Z1, Z2, Z3", np.array([[1, 2], [3, 4], [5, 6]]), ["n", "m"])
]
@pytest.mark.parametrize(parametrize_vars, parametrize_struct)
def test_transform_class(N1: int, N2: int, x_name: str, y_name: str, z_name: str, system: str) -> None:
    ### Create instance of transform
    transform = Transform

    ### Test images for variables
    system_new = transform.get_system()
    coeffs_new = transform.get_coeffs()
    coeffs_names_new = transform.get_coeffs_names()
    indices_new = transform.get_indices()
    indices_names_new = transform.get_indices_names_new()
    assert system_new == system
    assert coeffs_new == coeffs
    assert coeffs_names_new == coeffs_names
    assert indices_new == indices
    assert indices_names == indices_names
    assert np.shape(data_new) == (len(coord_names_new), N1 * N2)

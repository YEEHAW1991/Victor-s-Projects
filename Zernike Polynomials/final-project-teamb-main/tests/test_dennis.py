import pytest
import numpy as np
from src.ImageFactory import ImageFactory, ZeroImage, OneImage, RandomImage

def test_zero_image():
    coord_names = ['x', 'y']
    system = 'cartesian'
    zero_image = ImageFactory.create('zero', variant='predefined', coord_names=coord_names, system=system)
    assert isinstance(zero_image, ZeroImage)
    data = zero_image.get_data()
    assert np.all(data == 0)

def test_one_image():
    coord_names = ['x', 'y']
    system = 'cartesian'
    one_image = ImageFactory.create('one', variant='predefined', coord_names=coord_names, system=system)
    assert isinstance(one_image, OneImage)
    data = one_image.get_data()
    assert np.all(data == 1)

def test_random_image():
    coord_names = ['x', 'y']
    system = 'cartesian'
    random_image = ImageFactory.create('random', variant='random', coord_names=coord_names, system=system)
    assert isinstance(random_image, RandomImage)
    data = random_image.get_data()
    assert data.shape[0] == len(coord_names)
    assert np.all((0 <= data) & (data <= 1))

def test_invalid_predefined_name():
    coord_names = ['x', 'y']
    system = 'cartesian'
    with pytest.raises(ValueError, match="Predefined setting 'invalid' not found"):
        ImageFactory.create('invalid', variant='predefined', coord_names=coord_names, system=system)

def test_missing_coord_names_random():
    system = 'cartesian'
    random_image = ImageFactory.create('random', variant='random', system=system)
    assert isinstance(random_image, RandomImage)
    assert random_image.get_coord_names() == ['x', 'y']

def test_missing_coord_names_predefined():
    system = 'cartesian'
    zero_image = ImageFactory.create('zero', variant='predefined', system=system)
    assert isinstance(zero_image, ZeroImage)
    assert zero_image.get_coord_names() == ['x', 'y']

def test_polar_coordinates():
    coord_names = ['r', 'theta']
    system = 'polar'
    random_image = ImageFactory.create('random', variant='random', coord_names=coord_names, system=system)
    assert isinstance(random_image, RandomImage)
    assert random_image.get_coord_names() == coord_names
    assert random_image.get_system() == system

#for testing the predefine image in image class

def test_zero_image_im():
    coord_names = ['x', 'y']
    system = 'cartesian'
    zero_image = ZeroImage(coord_names=coord_names, system=system, N=100)
    data = zero_image.get_data()
    assert isinstance(zero_image, ZeroImage)
    assert data.shape == (len(coord_names), 100)
    assert np.all(data == 0)

def test_one_image_im():
    coord_names = ['x', 'y']
    system = 'cartesian'
    one_image = OneImage(coord_names=coord_names, system=system, N=100)
    data = one_image.get_data()
    assert isinstance(one_image, OneImage)
    assert data.shape == (len(coord_names), 100)
    assert np.all(data == 1)

def test_random_image_im():
    coord_names = ['x', 'y']
    system = 'cartesian'
    random_image = RandomImage(coord_names=coord_names, system=system, N=100)
    data = random_image.get_data()
    assert isinstance(random_image, RandomImage)
    assert data.shape == (len(coord_names), 100)
    assert np.all((0 <= data) & (data <= 1))

def test_random_image_default_N():
    coord_names = ['x', 'y']
    system = 'cartesian'
    random_image = RandomImage(coord_names=coord_names, system=system)
    data = random_image.get_data()
    assert isinstance(random_image, RandomImage)
    assert data.shape[0] == len(coord_names)
    assert data.shape[1] >= 50 and data.shape[1] <= 200
    assert np.all((0 <= data) & (data <= 1))
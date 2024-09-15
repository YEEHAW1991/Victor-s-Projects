import pytest
import numpy as np
import random
from Image import Image
from transform_verb import Transform


chooser = random.randint(1, 2) #randomly chooses to make a cartesian (1) or polar (2) image
if chooser == 1:
    print("Cartesian Image")
else:
    print("Polar Image")

#setting image coordinate data
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
d = random.randint(1,10)
e = random.randint(1,10)
f = random.randint(1,10)

@pytest.fixture
def image(): #makes an image
    if chooser == 1:
        image_data = np.array([[a, b, c], [d, e, f]])
        return Image(image_data, ['x', 'y'], 'cartesian')
    elif chooser == 2:
        image_data = np.array([[a, b, c], [np.pi/d, np.pi/e, np.pi/f]])
        return Image(image_data, ['rho', 'phi'], 'polar')

def test_rotate(image): 
    if chooser == 1:
        rotated = Transform.rotate(image, 90)
        expected_rotated = np.array([[d, a], [e, b], [f, c]])
        assert np.array_equal(rotated, expected_rotated)
    elif chooser == 2:
        rotated = Transform.rotate(image, 45)
        expected_rotated = np.array([[a, b, c], [np.pi/d + np.radians(45), np.pi/e + np.radians(45), np.pi/f + np.radians(45)]])
        assert np.array_equal(rotated, expected_rotated)

def test_flip(image):
    if chooser == 1:
        flipped = Transform.flip_transform(image, 'x')
        expected_flipped = np.array([[d, e, f], [a, b, c]])
        assert np.array_equal(flipped, expected_flipped)
        flipped = Transform.flip(cartesian_image, 'y')
        expected_flipped = np.array([[c, b, a], [f, e, d]])
        assert np.array_equal(flipped, expected_flipped)
    elif chooser == 2:
        flipped = Transform.flip_transform(image, 'x')
        expected_flipped = np.array([[a, b, c], [-np.pi/d, -np.pi/e, -np.pi/f]])
        assert np.array_equal(flipped, expected_flipped)
        flipped = Transform.flip_transform(image, 'y')
        expected_flipped = np.array([[c, b, a], [-np.pi/f, -np.pi/e, -np.pi/d]])
        assert np.array_equal(flipped, expected_flipped)

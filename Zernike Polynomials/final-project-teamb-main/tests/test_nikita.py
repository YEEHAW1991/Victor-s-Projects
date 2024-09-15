import numpy as np
import pytest
from Image import Image
from transform import Transform

parametrize_vars = "N1,N2,x_name,y_name,z_name,system"
parametrize_struct = [
    (100, 100, "X (mm)", "Y (mm)", "Power (W)", "cartesian"),
    (100, 100, "R (mm)", "Theta (rad)", "Power (W)", "polar")
]
@pytest.mark.parametrize(parametrize_vars, parametrize_struct)
def test_image_class(N1: int, N2: int, x_name: str, y_name: str, z_name: str, system: str) -> None:
    '''
    Test the basic image class
    After creating an instance of image, check for expected variables
    '''

    ### Generate sample variables
    intensity = np.random.rand(N1, N2) # Create z array of size N
    if system == "cartesian":
        x = np.linspace(0, N1, N1)
        y = np.linspace(0, N2, N2)
        x, y = np.meshgrid(x, y) # Create x and y coords for z data
    else:
        r = np.linspace(0, N1, N1) # Create r vector
        theta = np.linspace(0, 2*np.pi, N1) # Create theta vector
        x, y = np.meshgrid(r, theta) # Create r and theta coords for z data
    coord_names = [x_name, y_name, z_name] # Create list for coordinate names
    x = x.reshape((1, -1)) # Reshape into 1D array
    y = y.reshape((1, -1)) # Reshape into 1D array
    intensity = intensity.reshape((1, -1)) # Reshape into 1D array
    coords = np.array([x[0,:], y[0,:]]) # Create 2D array for coordinates

    ### Create instance of image
    image = Image(intensity, coords, coord_names, system)

    ### Test images for variables
    intensity_new = image.get_intensity()
    coords_new = image.get_coords()
    coord_names_new = image.get_coord_names()
    system_new = image.get_system()
    assert (coords_new == coords).all()
    assert coord_names_new == coord_names
    assert system_new == system
    assert np.shape(coords) == (len(coord_names_new)-1, N1 * N2)

def test_toZernike() -> None:
    '''
    Test the toZernike function
    Input will be an Image class instance and the transform parameters
    Output will be a Transform class instance
    '''
    from toZernike import toZernike
    from zernpy import ZernPol, fit_polynomials_vectors

    ### Create instance of Image class in polar coords
    N = 100

    intensity = np.random.rand(N, N) # Create z array of size N
    r = np.linspace(0, 1, N) # Create r vector
    theta = np.linspace(0, 2*np.pi, N) # Create theta vector

    r, theta = np.meshgrid(r, theta) # Create r and theta coords for z data

    r = r.reshape((1, -1))
    theta = theta.reshape((1, -1))
    intensity = intensity.reshape((1, -1))

    coords = np.array([r[0,:], theta[0,:]]) # Create 2D array for coords

    image_pol = Image(intensity, coords, ["R (mm)", "Theta (rad)", "Power (W)"], "polar")

    ### Setup Zernike polynomials
    N = 20 # Maximum OSA order for Zernike polynomials
    osa_indices = np.linspace(0, N, N+1, dtype=int) # Generate array of OSA order indices

    ### Call new toZernike function
    transform_zern = toZernike(image_pol, osa_indices) # Call toZernike with polar image and Zernike OSA indices

    ### Create transform from image class and OSA indices
    # Create tuple of given polynomials
    polynomials = []
    m = np.zeros(N+1, dtype=int)
    n = np.zeros(N+1, dtype=int)
    for i, osa_index in enumerate(osa_indices):
        zern = ZernPol(osa_index=osa_index)
        polynomials.append(zern)
        m_new, n_new = zern.get_mn_orders()
        m[i] = m_new
        n[i] = n_new

    # Fit image to polynomials and get coefficients
    intensity = image_pol.get_intensity()
    coords_new = image_pol.get_coords()
    coeffs = fit_polynomials_vectors(tuple(polynomials), intensity, coords_new[0,:], coords_new[1,:])

    # Check Transform class for expected variables
    assert transform_zern != None
    assert transform_zern.system == "Zernike"
    assert transform_zern.coeffs == coeffs
    assert transform_zern.coeffs_names == "Z"
    assert transform_zern.indices == np.array([m, n])
    assert transform_zern.indices_names == ["m", "n"]

def test_fromZernike() -> None:
    '''
    Test the fromZernike function
    Input will be a Transform class instance and the image parameters
    Output will be an Image class instance
    '''
    from fromZernike import fromZernike
    from zernpy import ZernPol

    ### Create instance of transform class for Zernike
    N = 10 # Number of coefficients
    coeffs = np.random.rand(N) # Zernike coefficients
    osa_indices = np.linspace(0, N-1, N) # OSA indices for coefficients
    indices = np.zeros((2, N))
    polynomials = []
    for i, osa_index in enumerate(osa_indices):
        polynomials[i] = ZernPol(osa_index=osa_index)
        indices[i,:] = polynomials[i].get_mn_orders()
    transform_zern = Transform("Zernike", coeffs, "Z", indices, ["m", "n"])

    ### Call new fromZernike function
    r_step = 0.01
    theta_step = np.pi/180
    image_pol = fromZernike(transform_zern, r_step, theta_step)

    ### Create image from transform
    z, r, theta = ZernPol.gen_zernikes_surface(coeffs.tolist(), polynomials, r_step=r_step, theta_rad_step=theta_step)

    ### Check image class for expected variables
    assert image_pol != None
    assert (image_pol.get_intensity() == np.array([z])).all()
    assert (image_pol.get_coords() == np.array([r, theta])).all()
    assert image_pol.get_coord_names() == ["R", "Theta", "Z"]
    assert image_pol.get_system() == "polar"

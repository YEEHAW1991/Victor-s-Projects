from Image import Image
from transform import Transform
from ImageFactory import ImageFactory
import numpy as np
from zernpy import ZernPol

def fromZernike(transform_zern: Transform, r_step: float, theta_step: float) -> None | Image:
    '''
    Function for creating a polar image class from a Zernike transform

    Parameters
    ----------
    transform_zern: Instance of Image class of the data in polar coordinates
    osa_indices: 1D numpy array of integers of the OSA indices to perform the Zernike fit

    Returns
    -------
    transform_zern: Instance of Transform class of the Zernike fit
    '''

    ### Check for correct transform type
    system = transform_zern.get_system().upper().strip()
    assert system == "ZERNIKE", f"Inverse Zernike transform is not supported for {system} transforms"

    ### Construct polynomials from coefficients and indices
    coeffs = transform_zern.get_coeffs() # 1D array of coefficients
    indices = transform_zern.get_indices() # 2D array of m, n indices
    polynomials = [ZernPol(n=index[1], m=index[0]) for index in indices] # Populate polynomial list

    ### Create image from transform
    z, r, theta = ZernPol.gen_zernikes_surface(coeffs.tolist(), polynomials, r_step=r_step, theta_rad_step=theta_step)
    z = np.array([z])
    coords = np.array([r, theta])

    ### Create image class from polar vectors
    return ImageFactory.create("Polar", "data", intensity=z, coords=coords, coord_names=["R", "Theta", "Z"], system="polar")

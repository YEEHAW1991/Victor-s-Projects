from Image import Image
from transform import Transform
from TransformFactory import TransformFactory
import numpy as np
from zernpy import ZernPol, fit_polynomials_vectors

def toZernike(image_pol: Image, osa_indices: np.ndarray) -> None | Transform:
    '''
    Function for creating a Zernike transform class from a image in polar coordinates

    Parameters
    ----------
    image_pol: Instance of Image class of the data in polar coordinates
    osa_indices: 1D numpy array of integers of the OSA indices to perform the Zernike fit

    Returns
    -------
    transform_zern: Instance of Transform class of the Zernike fit
    '''

    # Create structures for polynomials, m, and n indices
    polynomials = [] # Initialize list for polynomials
    m = n = np.zeros_like(osa_indices, dtype=int) # Initialize array for m and n indices
    for i, osa_index in enumerate(osa_indices):
        # Loop over osa_indices and fill polynomial, m, and n structures
        zernike = ZernPol(osa_index=osa_index)
        polynomials.append(zernike)
        m_new, n_new = zernike.get_mn_orders()
        m[i] = m_new
        n[i] = n_new

    # Fit polynomials from image vector data
    intensity = image_pol.get_intensity()
    coords = image_pol.get_coords()
    coeffs = fit_polynomials_vectors(tuple(polynomials), intensity, coords[0,:], coords[1,:])

    # Create transform class using transform coefficients
    return TransformFactory.create_transform("Zernike", "data", np.array([coeffs, m, n]), ["Z", "m", "n"], "polar")

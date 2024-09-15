import numpy as np
from Image import Image
from transform import Transform
from scipy.fft import fft2, fftshift



class toFFT:
    @staticmethod
    def toFFT(image: Image, **params) -> Transform:
        #getting intensity data
        intensity = image.get_intensity()

        # perform 2D FFT and shift the zero frequency component to the center
        fft_coeffs = fftshift(fft2(intensity))

        # Create frequency coordinates
        M, N = intensity.shape
        freq_x = np.fft.fftfreq(M, d=1)
        freq_y = np.fft.fftfreq(N, d=1)

        # Create meshgrid of frequency coordinates
        freq_x, freq_y = np.meshgrid(freq_x, freq_y)

        # Create the Transform object
        transform = Transform(
            system='frequency',
            coeffs=fft_coeffs,
            coeffs_names=['fft_coeffs'],
            indices=np.array([freq_x, freq_y]),
            indices_names=['freq_x', 'freq_y']
        )

        return transform

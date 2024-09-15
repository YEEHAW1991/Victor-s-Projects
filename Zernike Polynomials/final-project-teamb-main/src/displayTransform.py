import numpy as np
from Transform import Transform
<<<<<<< HEAD
import matplotlib.pyplot as plt

class displayTransform():
    @staticmethod
    def display(Transform, plot_type):
        #pretty much straight from the display image part
        data = Transform.data
        if transform.system == 'Zernike':
            x, y = displayTransform.polar_to_cartesian(data[0], data[1])
            data = np.stack([x, y])
        elif transform.system == 'DFT':
            fft_data = np.fft.fft2(data)
            x, y = fft_data.real, fft_data.imag
            data = np.stack([x, y])
        else:
            raise ValueError("Enter either Zernike or DFT (case sensitive)")
            
        if plot_type == 'intensity':
            plt.imshow(data, cmap = 'gray')
        elif plot_type == 'heatmap':
            plt.imshow(data, cmap = 'hot')
        else:
            raise ValueError("invalid plot type")
        plt.show()
        
    @staticmethod
    def polar_to_cartesian(r, theta):
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        return x, y

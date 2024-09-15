import numpy as np
import random

class TransformFactory:
    '''
    TransformFactory class for creating Transform instances with predefined or random settings
    '''
    _Transform = {
        #adding transform predefine data
    }

    @staticmethod
    def create_transform(name, variant: str = 'random', data: np.ndarray =  None, coeff_names: list = None, system: str = 'cartesian'):
        '''
        Creates a Transform instance from the provided data array.

        Parameters
        ----------
        name: transform name
        variant :  specifies whether to create a random transform or from the provided data array
        data : (optional) 1D or 2D numpy array containing the coefficients or transformation matrix.
        coeff_names : list of strings representing the names of the coefficients.
        system: describes the transformation system used, such as 'cartesian' or 'polar'.
            Default is 'cartesian'.
        '''
        if variant == 'random':
            # generate random data
            N = random.randint(5, 20)  # random number of coefficients
            if not coeff_names:
                coeff_names = [f'coeff_{i}' for i in range(N)]
            data = np.random.rand(N)
        else:
            # use predefine data
            if data is None or coeff_names is None:
                raise ValueError("Data and coeff_names are empty for predefined setting")
            if len(coeff_names) != data.shape[0]:
                raise ValueError("length of coeff_names not match the first dimension of data")
        
        return TransformFactory._Transform[name](data=data, coeff_names=coeff_names, system=system)
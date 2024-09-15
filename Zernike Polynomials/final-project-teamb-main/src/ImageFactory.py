import numpy as np
from Image import Image, ZeroImage, OneImage, RandomImage



class ImageFactory:
    '''
    ImageFactory class for create image instances with predefined settings or randomly generated data
    '''
    _Image = {
        'zero': ZeroImage,
        'one': OneImage,
        'random': RandomImage,
        #adding more predefined images as needed
    }

    """
    meeting notes
    write subclass that all 000 and all 111
    argument: variant, param
    uniform tell the intensity
    kind, param, standard
    coordinate name, coordinate"""
    
    """ditch that all together, standard for coordinate name, only X, Y"""
    #The image should not contain the information that display
    

    @staticmethod
    def create(name, variant: str = 'predefined', data: np.ndarray = None, coord_names: list = None, system: str = 'cartesian'):
        '''
        Parameters
        ----------
        name: model name
        variant : Specifies whether to create a random Image or from the provided data array
        data : (or optional) 2D numpy array of shape (len(coord_names), N) where N is the number of data points.
        coord_names : list of strings of the coordinate names in data
        system : describes the coordinate system, either 'cartesian' or 'polar'
            Default: 'cartesian'
        '''
        if variant == 'random':
            if not coord_names:
                coord_names = ['x', 'y'] if system == 'cartesian' else ['r', 'theta']
            return RandomImage(coord_names=coord_names, system=system)
        else:
            if name not in ImageFactory._Image:
                raise ValueError(f"Predefined setting '{name}' not found")
            if not coord_names:
                coord_names = ['x', 'y'] if system == 'cartesian' else ['r', 'theta']
            return ImageFactory._Image[name](coord_names=coord_names, system=system)    

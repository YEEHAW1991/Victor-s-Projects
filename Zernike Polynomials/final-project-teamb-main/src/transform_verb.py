import numpy as np
from Image import Image


class Transform():
        
    '''
    Image is the image that is given
    Angles is given in degrees
    '''
    @staticmethod
    def rotate(image: 'Image', angles: float) -> np.ndarray:
        radians = np.radians(angles) #converts the degrees into radians
        
        #gets input from the Images class
        image_data = image.get_data()
        system = image.get_system()
        
        if system == "polar": 
            rotated = image_data + radians   
        elif system == "cartesian":
            rotation_matrix = np.array([[np.cos(radians), -np.sin(radians)],[np.sin(radians), np.cos(radians)]])
            rotated = np.matmul(rotation_matrix, image_data)
        else:
            raise ValueError("Please enter a either polar or cartesian coordinates in all lowercase.")
        return rotated
    
    '''
    Image is the image that is given
    Axis is either 'x' or 'y'
    '''
    @staticmethod
    def flip_transform(image: Image, axis: str) -> np.ndarray:
        #gets input from the Images class
        image_data = image.get_data()
        system = image.get_system()
        flip = None #this is the main thing that is getting flipped.
        
        if system == "cartesian":
            if axis == 'x':
                flip = np.fliplr(image_data)
            elif axis == 'y':
                flip = np.flipup(image_data)
            else:
                raise ValueError("Please enter either x or y as your axis in lowercase.")
        elif system == "polar":
            if axis == 'x':
                flip = np.array([image_data[0], -image_data[1]])
            elif axis == 'y':
                flip = np.array([-image_data[0], image_data[1]])
            else:
                raise ValueError("Please enter either x or y as your axis in lowercase.")
        if flip is None:
            raise ValueError("Could not flip this.")
        return flip
        

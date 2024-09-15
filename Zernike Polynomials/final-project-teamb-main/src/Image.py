import numpy as np
import random


class Image():
    '''
    Image class describing the data and format of images
    '''

    def __init__(self, intensity: np.ndarray, coords: np.ndarray, coord_names: list, system: str) -> None:
        '''
        Parameters
        ----------
        intensity
            2D numpy array of shape (M, N) where N is the
            total number of data points and M varies based
            on pixel data format
        coords
            2D numpy array of shape (len(coord_names)-len(intensity), N)
            where N is the total number of data points
        coord_names
            list of strings of the coordinate names in coords
            and intensity
        system
            String describing coordinate system,
            either "cartesian" or "polar"
        '''

        self.__intensity = intensity
        self.__coords = coords
        self.__coord_names = coord_names
        self.__system = system

    def get_intensity(self) -> np.ndarray:
        '''
        Return the intensity data in numpy 2D array format

        Returns
        -------
        intensity
            2D numpy array of shape (M, N) where N is the
            total number of data points and M varies based
            on pixel data format
        '''
        return self.__intensity

    def get_coords(self) -> np.ndarray:
        '''
        Return the coordinate data in numpy 2D array format

        Returns
        -------
        coords
            2D numpy array of shape (len(coord_names)-len(intensity), N)
            where N is the total number of data points
        '''
        return self.__coords

    def get_coord_names(self) -> list:
        '''
        Return the coordinate names for dim 1 of coords and intensity

        Returns
        -------
        coord_names
            list of strings of the coordinate names in coords and intensity
        '''
        return self.__coord_names

    def get_system(self) -> str:
        '''
        Return the coordinate system for the image

        Returns
        -------
        system
            String describing coordinate system,
            either "cartesian" or "polar"
        '''
        return self.__system
    
class ZeroImage(Image):
    '''
    Image subclass generating data arrays filled with 0s
    '''
    def __init__(self, coord_names: list, system: str, N: int = 100) -> None:
        intensity = np.zeros((len(coord_names), N))
        data = np.zeros((len(coord_names), N))
        super().__init__(intensity, data, coord_names, system)

class OneImage(Image):
    '''
    Image subclass generating data arrays filled with 1s
    '''
    def __init__(self, coord_names: list, system: str, N: int = 100) -> None:
        intensity = np.ones((len(coord_names), N))
        data = np.ones((len(coord_names), N))
        super().__init__(intensity, data, coord_names, system)

class RandomImage(Image):
    '''
    Image subclass generating random data arrays
    '''
    def __init__(self, coord_names: list, system: str, N: int = None) -> None:
        if N is None:
            N = random.randint(50, 200)  # random number of data points
        intensity = np.random.rand(len(coord_names), N)
        data = np.random.rand(len(coord_names), N)
        super().__init__(intensity, data, coord_names, system)
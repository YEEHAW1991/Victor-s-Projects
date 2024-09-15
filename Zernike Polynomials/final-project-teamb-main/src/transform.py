#actual transform (the noun) not verb 


import numpy as np
from typing import List

class Transform():
    
    def __init__(self, system: str, coeffs: str, coeffs_names: str, indices: np.ndarray, indices_names: List[str]):
        '''
        Parameters:
        
        system = the name of the system, whether it's Zernike or DFT
        coeffs = the coefficients
        coeffs_names = the names of the coefficients
        indices = the indices
        indices_names = the names of the indices
        '''
        
        self._system = system
        self._coeffs = coeffs
        self._coeffs_names = coeffs_names
        self._indices = indices
        self._indices_names = indices_names
    
    def get_system(self) -> str:
        #returns the system name
        return self._system
    
    def get_coeffs(self) -> str:
        #returns the coefficients
        return self._coeffs
    
    def get_coeffs_names(self) -> str:
        #returns the names of the coefficients
        return self._coeffs_names
    
    def get_indices(self) -> np.ndarray:
        #returns the indices
        return self._indices
    
    def get_indices_names(self) -> List[str]:
        #returns the names of the indices
        return self._indices_names


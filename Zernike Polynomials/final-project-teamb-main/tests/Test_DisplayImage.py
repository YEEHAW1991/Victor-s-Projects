from DisplayImage import Image, DisplayImage
import numpy as np

from unittest.mock import patch
import pytest  

@patch('matplotlib.pyplot.imshow')  
@patch('matplotlib.pyplot.show')  
def test_display_polar_intensity(mock_show, mock_imshow):   
    r = np.array([1, 2, 3])  
    theta = np.array([np.pi / 4, np.pi / 2, 3 * np.pi / 4])  
    coords = np.column_stack((r, theta))  
    image = Image(np.zeros((10, 10)), coords, ['r', 'theta'], 'polar')  

    DisplayImage.display(image, 'intensity')  
  
    mock_imshow.assert_called_once()  

    assert isinstance(mock_imshow.call_args[0][0], np.ndarray)  
  

    mock_show.assert_called_once()  
  
@patch('matplotlib.pyplot.imshow')  
@patch('matplotlib.pyplot.show')  
def test_display_non_polar_heatmap(mock_show, mock_imshow):  
 
    data = np.random.rand(10, 10)  
    image = Image(data, None, None, 'cartesian')  
   
    DisplayImage.display(image,'heatmap')  
    
    mock_imshow.assert_called_once_with(data, cmap='hot')
    
    mock_show.assert_called_once()  
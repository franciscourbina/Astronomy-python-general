import numpy as np 
import astropy.io.fits as F 


def wavearr(data_path, data_ind=1):
    """
    Given a path to a cube, it calculates the wavelength array.
    """

    hdu = F.open(data_path)
    header = hdu[data_ind].header
    
    dlamb = header['CD3_3']
    lamb0 = header['CRVAL3']
    nw = header['NAXIS3']

    return np.arange(0, nw) * dlamb + lamb0


def circular_aperture_spectrum(data, variance, position, radius):
    """
    Radius is given in pixels.
    """ 
    # Create circular mask
    nw, nx, ny = data.shape

    xx, yy = np.mgrid[:nx, :ny]
    circle = (xx - position[0]) ** 2 + (yy - position[1]) ** 2
    circle = circle < (radius)**2

    spectrum = np.nansum(data * circle[np.newaxis,:,:], axis=(1,2)) 
    error = np.sqrt(np.nansum(variance * circle[np.newaxis,:,:], axis=(1,2))) 

    return spectrum, error

def write_spectrum_file(spectrum, final_path, dlamb=1.25):
    pass
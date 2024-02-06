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


def circular_aperture_spectrum(data_path, position, radius, data_ind=1, var_ind=2):
    """
    Radius is given in pixels.
    """ 

    hdu = F.open(data_path)
    data = hdu[data_ind].data
    variance = hdu[var_ind].data

    # Create circular mask
    nw, nx, ny = data.shape

    xx, yy = np.mgrid[:nx, :ny]
    circle = (xx - position[0]) ** 2 + (yy - position[1]) ** 2
    circle = circle < (radius)**2

    spectrum = np.nansum(data * circle[np.newaxis,:,:], axis=(1,2)) 
    error = np.sqrt(np.nansum(variance * circle[np.newaxis,:,:], axis=(1,2))) 

    return spectrum, error

def write_spectrum_file(flux, errors, wavelength, final_path):
    """
    Write the spectrum in a simple 3-column table fits format.
    """

    col1 = F.Column(name='Flux', format='D', array= flux)
    col2 = F.Column(name='Error', format='D', array=errors)
    col3 = F.Column(name='Wave', format='D', array=wavelength)
    cols = F.ColDefs([col1, col2, col3])

    table_hdu = F.BinTableHDU.from_columns(cols)
    
    table_hdu.writeto(final_path)

def compute_magnitude():
    """
    To be done
    """
    pass
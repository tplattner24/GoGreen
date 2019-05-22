import numpy as np
from astropy.table import Table
from astropy.io import ascii


def catread(clname, photext):
    PATH = '/Users/taylorplattner/Work/GoGreen/Data/Releases/v1.0/v1.0/PHOTOMETRY/'
    rfname = PATH + 'RESTFRAME_COLOURS/RESTFRAME_MASTER_' + '.clname' + '_indivredshifts.cat'
    photname = PATH + 'PHOTOM.CATS/' + '.clname' + '_totalall_' + photext[clname] + '.cat'
    rfcat = table.read(rfname)
    photcat = table.read(photname)
    return(rfcat, photcat)

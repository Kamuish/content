from astropy.io import fits

wave_mask, cont_mask = [], []

with fits.open("ESPRESSO_G9.fits") as hdu:
    data = hdu[1].data

    for entry in data:
        wave_mask.append(entry[0])
        cont_mask.append(entry[1])

import matplotlib.pyplot as plt

plt.switch_backend("TkAgg")


with fits.open(
    "/home/amiguel/class_simulations/real_spectra/r.ESPRE.2021-10-25T06:06:31.460_S2D_A.fits"
) as hdu:
    wave = hdu[4].data
    sci = hdu[1].data

    err = hdu[2].data

plt.scatter(wave_mask, cont_mask)


from PyAstronomy import pyasl
import numpy as np

wave_mask = np.asarray(wave_mask)
cont_mask = np.asarray(cont_mask)

plt.figure()

for order in range(40, 88, 2):

    inds = np.where(sci[order] != 0)
    rv, cc = pyasl.crosscorrRV(
        wave[order][inds],
        sci[order][inds],
        wave_mask,
        cont_mask,
        40.0,
        100.0,
        0.5,
        skipedge=50,
    )
    plt.plot(rv, cc)
plt.show()

from pathlib import Path
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

plt.switch_backend("TkAgg")
dark_folder = Path(".").absolute() / "darks"
bias_folder = Path(".").absolute() / "bias"
flat_folder = Path(".").absolute() / "flats"
inject_folder = Path(".").absolute() / "injection"
real_folder = Path(".").absolute() / "real_spectra"
simulated_raws = Path(".").absolute() / "products"


def order_extraction(image, head):

    N_ORDERS = head["N_ORDERS"]
    ORDER_width = head["ORDER_width"]
    ORDER_SPACING = head["ORDER_SPACING"]

    sci = np.zeros((N_ORDERS, image.shape[1]))
    start = head["CCD PIXEL OFFSET"]

    for order in range(N_ORDERS):
        sci[order] = np.sum(image[start : start + ORDER_width, :], axis=0)
        start = start + ORDER_width + ORDER_SPACING
    return sci


def construct_master_calib(folder, method="median"):
    all_darks = list(folder.glob("*.fits"))
    N_darks = len(all_darks)

    for index, file in enumerate(all_darks):
        with fits.open(file) as hdu:
            dark = hdu[0].data

        if index == 0:
            data_cube = np.zeros((N_darks, *dark.shape))
        data_cube[index] = dark

    if method == "median":
        master_dark = np.median(data_cube, axis=0)
    return master_dark


m_dark = construct_master_calib(dark_folder)
# # m_bias = construct_master_calib(bias_folder)
m_flat = construct_master_calib(flat_folder)

# m_flat = m_flat - m_dark  # Remove dark contribution + BIAS level
median_level = np.nanmedian(m_flat[np.where(m_flat > 0)])
# m_flat /= median_level  # Normalize the flat file!!
print(np.median(m_flat), np.min(m_flat), np.max(m_flat))

with fits.open(simulated_raws / "raw_0.fits") as hdu:
    head = hdu[0].header
    wave = hdu[0].data
    raw_science = hdu[1].data
    truth_science = hdu[2].data
# truth_science -= np.median(truth_science)

plt.imshow(np.log(raw_science - np.median(raw_science)), cmap="coolwarm", aspect="auto")

plt.ylim([1300, 1500])
no_calib_spectra = order_extraction(raw_science, head)

print(m_dark.shape)

print(raw_science)
plt.figure()

for i in range(wave.shape[0]):
    plt.scatter(wave[i], no_calib_spectra[i])

plt.show()

calibrated_file = raw_science - m_dark
calib_spectra_no_FLAT = order_extraction(calibrated_file, head)

calibrated_file /= m_flat

calib_spectra = order_extraction(calibrated_file, head)

print(no_calib_spectra.shape)
# calibrated_file = (raw_science - m_dark) / m_flat

#


# no_calib_spectra -= np.median(no_calib_spectra)
# truth_science -= np.median(truth_science)
# calib_spectra -= np.median(calib_spectra)

# no_calib_spectra[no_calib_spectra > 0] = np.nan
# no_calib_spectra -= np.nanmedian(no_calib_spectra)

# calib_spectra -= np.median(calib_spectra)

fig = plt.figure()
axis = plt.gca()
axis.set_title("comparison")
axis.scatter(wave[0], no_calib_spectra[0], color="red")
axis.scatter(wave[0], calib_spectra[0], color="blue")
axis.scatter(wave[0], calib_spectra_no_FLAT[0], color="orange", s=9)

# axis.scatter(wave[0], calib_spectra[0], color="black")

axis.plot(wave[0], truth_science[0], color="green", ls="--")

plt.figure()
plt.title("residuals")
plt.scatter(wave[0], truth_science[0] - no_calib_spectra[0])

plt.figure()
plt.scatter(wave[0], calib_spectra[0], color="blue")
plt.show()

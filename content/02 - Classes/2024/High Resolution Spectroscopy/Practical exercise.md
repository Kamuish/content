---
tags:
  - classes/physics
  - fcup/PDA
  - year/2024
draft: false
---

# Practical exercise:

## Description of the project

You are provided with a science image and calibration frames. 

The goals are:

1) Use the calibration images to calibrate the science image;
2) Extract the spectra from the raw image and compare it against one obtained from non-calibrated images;
3) Compare the retrieved spectra against the injected one (see [[#^ab45d2|Data description for details]])

Without using the data, discuss the following topics:

- Do you see any advantage/disadvantage of using the same calibration frame to mitigate the dark current effects and the read noise?
- What could be done to account for a possible difference in exposure time between the science exposure and the *dark* calibration?


## Data description

^ab45d2

- You have access to the following (simulated) data products:

1) 1 raw image, with the science observations
2) 20 dark frames
3) 20 bias frames
4) 20 flat frames

**Data format:** Every image is provided as a [[Fits files|fits file]].

**Raw image:**  Each spectral order is horizontal on the detector with a separation of  *ORDER_SPACING* and occupying a width of *ORDER_width*. The first order (on the CCD) only starts after *overscan* pixels. The wavelengths associated with each pixel of each order are already provided. The injected spectra (i.e., the *truth*) is also provided.

The data can be accessed in the following way (through python):
```python
from astropy.io import fits 

your_path_to_raw_file = "raw_0.fits"
with fits.open(your_path_to_raw_file) as hdu:
	head = hdu[0].header
	wavelength = hdu[0].data
	raw_science = hdu[1].data
	truth = hdu[2].data
	
	N_ORDERS = head["N_ORDERS"]
	ORDER_width = head["ORDER_width"]
	ORDER_SPACING = head["ORDER_SPACING"]
	overscan = head["CCD PIXEL OFFSET"]
```


**Calibration images:** The images are provided in the same orientation as the raw image, they can be also opened through *astropy*:

```python
from astropy.io import fits 

your_path_to_calibration_file = "darks_0.fits"
with fits.open(your_path_to_calibration_file) as hdu:
	head = hdu[0].header
	calibration_data = hdu[0].data

```


## Assumptions:

1) The flat field observations have a very high SNR and we can ignore noise sources (read noise / dark current)
2) The darks were taken with the same exposure time as the science observations


## Evaluation:

1) Short presentation to present the work and findings (maximum 10 minute), will be counted as 50% of the grade;
2) Small report (maximum of 5 pages) of the project, which will count as the other 50% of the evaluation;
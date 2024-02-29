---
title: Análise de Dados em Física e Astronomia
draft: false
tags: classes/python, classes/physics, fcup/DFA, year/2024
---

# Análise de Dados em Física e Astronomia

Course page: https://sigarra.up.pt/fcup/pt/ucurr_geral.ficha_uc_view?pv_ocorrencia_id=527300

 e-mail: andsilva@fc.up.pt

---

## Work plan for the classes

- First 2 classes: refreshing the basics of *python*:
	- Basic Python
	- Scientific libraries: *Numpy* / *scipy*
	- Data visualization: *matplotlib*

- 1st project: **Fitting a spectral line**
- 2nd project: **Analysis of a RV time-series**
---

## Plan for the classes:

### Class 3: 05/03/2024

#### Relevant Documents:

- Astropy:
	- [notebook](astropy.ipynb);
	- [fits file for the notebook](resources/r.ESPRE.2019-07-24T00:09:54.984_S2D_BLAZE_A.fits);
	- [[Astropy|link with more details]]

#### Practical exercises:

*Median filter*:

**Why:** The need of estimating the continuum level of a signal/data is a problem often faced when dealing with stellar spectra. One possible tool to solve it is a median filter, a technique often used to remove noise from an image or signal. The main idea of this filter filter is to run through the signal entry by entry, replacing each entry with the median of neighbouring entries (window centred in each point, size must always be odd).

 **How:** The goal of this exercise is:

1) Create a function that implements a median filter with a window of size N, with a given boundary condition, and apply it to each spectral order of the observation. To account for boundary conditions **one** of the following (equal to those from scipy) can be selected:

	- reflect (d c b | a b c d | d c b a) - The input is extended by reflecting about the edge of the last pixel. This mode is also sometimes referred to as half-sample symmetric.
	- nearest (a a a a | a b c d | d d d d) - The input is extended by replicating the last pixel.
	- mirror (d c b | a b c d | c b a) - The input is extended by reflecting about the center of the last pixel. This mode is also sometimes referred to as whole-sample symmetric.
	- wrap (a b c d | a b c d | a b c d) - The input is extended by wrapping around to the opposite edge.

2) Open the [fits file](resources/r.ESPRE.2019-07-24T00:09:54.984_S2D_BLAZE_A.fits) and load ESPRESSO data.

3) Apply the median filter to each spectral order using different window sizes.

	1) Note: some ESPRESSO spectral orders are zero-padded due to the optical design of the instrument. That data should be removed/ignored before applying the filter

4) Plot the stellar spectra from one (or more) orders, alongside the output of the filter that you created;

5) Compare your results with those from scipy's [median filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.median_filter.html#scipy.ndimage.median_filter)

### Class 2: 27/02/2024

- [Numpy basics](Numpy.ipynb)
- [Scipy](Scipy.ipynb)
- [Data Visualization](DataVisualization.ipynb)

### Class 1: 20/02/2024

- [Basic Python](basicPython.ipynb)
- [[Virtual Environments]]
---

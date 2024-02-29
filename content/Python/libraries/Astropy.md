---
title: Astropy
draft: false
tags: python/library
---

# Astropy

## Handling fits files

Astropy also provides an easy interface to [[Fits files|fits files]] in python, allowing to access data from different instruments.

- Print overview of all extensions inside the fits file:
```python
from astropy.io import fits 

with fits.open(s2d_file) as hdu:
	print(hdu.info())
```

- Accessing the header of a given data unit, which is returned as a python dictionary:
```python
with fits.open(s2d_file) as hdu:
	header = hdu["PRIMARY"].header

```

- The extensions can be accessed through their keys, and the data units using the *.data* property
```python
with fits.open(s2d_file) as hdu:
	wavelength = hdu["WAVEDATA_VAC_BARY"].data
	fluxes = hdu["SCIDATA"].data
	uncertainties = hdu["ERRDATA"].data
```

### Command line scripts:

- [fitsinfo](https://docs.astropy.org/en/stable/io/fits/usage/scripts.html#module-astropy.io.fits.scripts.fitsinfo)
- [fitsheader](https://docs.astropy.org/en/stable/io/fits/usage/scripts.html#module-astropy.io.fits.scripts.fitsheader)


> [!NOTE] References
> https://docs.astropy.org/en/stable/
> https://docs.astropy.org/en/stable/io/fits/

# Handling units

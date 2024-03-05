---
title: Fits files
draft: false
tags: year/2024
---

# Fits files

Widely used data format in astrophysics, with the data of most instruments being stored in them. That said, their usage leads to large overheads due to its specifications.

One fits file can have multiple *extensions*, which are built from two different elements:

- Data unit - where tabular data and arrays are stored
- Headers - store data type and other miscellaneous information. Often used to store information related to the operations of the instrument and outputs of pipelines

These two elements, together, are called the **H**eader and **D**ata **U**nit (HDU). Both header and data units are stored in disk inside blocks with a size of 2880-byte. When doing so, there are two options:

- If the data takes more than one block, a new one starts where the previous one ends
- If the data is not enough to fill one block, the data is zero-padded until it fits.

## Interfaces to fits files:

- Through Python: [[Astropy#Handling fits files]]
- Other interfaces:
	- [fitsviewer](https://fits.gsfc.nasa.gov/fits_viewer.html) is a graphical interface
	- [dfits and fitsort](https://www.eso.org/sci/software/eclipse/eug/eug/node8.html) are command line options
	- [[Astropy]] provides *fitsheader* and *fitsinfo*


```ad-abstract
title: References
https://en.wikipedia.org/wiki/FITS
https://fits.gsfc.nasa.gov/
https://fits.gsfc.nasa.gov/standard40/fits_standard40aa-le.pdf
```

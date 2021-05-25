# 3D extinction maps of the southern sky

Based on the multi-band photometry of SkyMapper Southern Survey, Gaia DR2, the Two Micron All Sky Survey and the Wide-Field Infrared Survey Explorer Survey, we have estimated values of the r-band extinction for∼ 19 million stars with the spectral energy distribution (SED) analysis. Combined with the distances from the Gaia DR2 parallaxes, we have constructed a three-dimensional extinction map of the southern sky. The paper has been published by ApJ: https://ui.adsabs.harvard.edu/abs/2021ApJ...906...47G/abstract. This repository shows how to download the data underlying the article and how to use our 3D extinction maps.

If you have any questions or need more informations, please send emall to Bingqiu Chen (bchen@ynu.edu.cn) and Helong Guo (helong_guo@mail.ynu.edu.cn).


## Download the 3D extinction maps

The full data of our 3D extinction maps of the southern sky can be download here：https://doi.org/10.12149/101032

The file 'SkyMapperAr.fits' is the full data of our 3D extinction maps of the southern sky. Each row of the file contains the extinction profile for one line of sight: Galactic coordinates l, b along with the extinction values at the individual distances A_{r,0 kpc} (defined as 0 mag), A_{r,0.2 kpc}, A_{r,0.4 kpc}, A_{r,0.6 kpc}, A_{r,0.8 kpc} ... A_{r,5.8 kpc}, A_{r,6.0 kpc} and respective uncertainties.

## Query the 3D extinction maps

We have provided a simple PYTHON3 procedure '3Ddustmap.py', which can be used to query our extinction maps. The function 'southernskydust_map' in the procedure returns E(B-V) value for a given 3D position (l, b and d).

For example, if one want to obtain the extinction of a star at Galactic coordinates l = 300 deg, b = -15 deg and distance of 2.5 kpc:
```
import dustmap_3D as dm
l, b, d = 300.0, -15.0, 2.5
ebv = dm.southernskydust_map(l,b,d) 

```
which will return
```
ebv = 0.143
```

## Additional dataset

### Extinction values of 17 million stars 
In addition to the 3D extinction maps, we also provide the file 'SkyMapper_stellar_Ar.fits', which contains best fit extinction values for over 17 million stars in the southern sky. 

For each star, we provide its Galactic Coordinate (“l” and “b”), distance ("dis"), r-band extinction ("Ar") and the minimum chi-squre of the SED analysis ("chi2").


### All-sky 3D extinction maps

The file 'allskymap_EBV.fits' is an all-sky extinction maps, which combine our 3D extinction maps in the southern sky and those from the literature. Similar as the 3D extinction maps in the souther sky, the file contains a table. Each row of the table contains the extinction profile for one line of sight: Galactic coordinates l, b along with the reddening values at the individual distances E(B-V)_{0 kpc} (defined as 0 mag), E(B-V)_{0.2 kpc}, E(B-V)_{0.4 kpc}, E(B-V)_{0.6 kpc} ... E(B-V)_{5.8 kpc}, E(B-V)_{6.0 kpc}.

The function 'allskydust_map' in the procedure '3Ddustmap.py' can be used to return E(B-V) value for a given 3D position (l, b and d).

The function 'allskydust_map' in the procedure '3Ddustmap.py' can be used to return E(B-V) value for a given 3D position (l, b and d).

### The stellar loci
The files 'Dwarf_locus.fits' and 'Giant_locus.fits' are the selected 987,336 dwarfs and 146,957 giants which are adopted to construct the stellar loci of dwarfs and giants, respectively.






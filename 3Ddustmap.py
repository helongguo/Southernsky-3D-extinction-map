from astropy.io import fits
import numpy as np
from scipy import interpolate
from astropy import units as u		
from astropy.coordinates import SkyCoord

def southernskydust_map(l,b,d):
	guo2019=fits.open('SkyMapperAr.fits')
	L=guo2019[1].data.field('L')
	B=guo2019[1].data.field('B')
	D=np.arange(0.0,6.2,0.2)
	Rr=3.407
	Ar=guo2019[1].data.field('Ar')
	index=np.where((L>l-0.3) & (L<l+0.3) & (B>b-0.3) & (B<b+0.3) )[0]
	if len(index)==0 :
		EBV=np.nan
	else:
		l0=L[index]
		b0=B[index]
		ebv0=Ar[index]
		dismin=(l0-l)**2+(b0*np.cos(np.radians(b0))-b*np.cos(np.radians(b)))**2
		index1=np.where(dismin==np.min(dismin))
		l=l0[index1]
		b=b0[index1]
		EBV1=ebv0[index1]
		f=interpolate.interp1d(D,EBV1,kind='zero')
		EBV=f(d)/Rr
	
	print('input:l,b,d,unit=[deg,kpc],d<=5.8,fram=galactic,output:E(B-V)')
	return EBV


def allskydust_map(l,b,d):
	allskydustmap=fits.open('allskymap_EBV.fits')
	L=allskydustmap[1].data.field('L')
	B=allskydustmap[1].data.field('B')
	D=np.arange(0.0,6.2,0.2)
	ebv=allskydustmap[1].data.field('EBV')
	index2=np.where((L>l-0.3) & (L<l+0.3) & (B>b-0.3) & (B<b+0.3))[0]
	EBV3=southerndust_sky(l,b,d)
	if len(index2)==0:
		EBV=np.nan
	

	else:		
		l0=L[index2]
		b0=B[index2]
		ebv0=ebv[index2]
		dismin=(l0-l)**2+(b0*np.cos(np.radians(b0))-b*np.cos(np.radians(b)))**2
		index3=np.where(dismin==np.min(dismin))
		l=l0[index3]
		b=b0[index3]
		EBV1=ebv0[index3]
		f=interpolate.interp1d(D,EBV1,kind='zero')
		EBV=f(d)
		

	
	return EBV




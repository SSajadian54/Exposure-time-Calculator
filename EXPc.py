import numpy as np 
from astropy import units as u
import hmbp
################ CONSTANTS ####################################
area=51.2#[m^2] area of UT4-VLT telescope
velocity=299792458.0## light velocity [m/s]
hplanck=6.62607004*pow(10.0,-34.0)## [m2.kg/s]
kbol=1.380649*pow(10.0,-23)## Boltzman constant       
bb= float(8.0*np.pi*hplanck*velocity*velocity)
kpc= 3.0857*pow(10.0,19.0)## [m] 
nm=0.000000001## nano meter to meter 
pix_s=0.106 ##pixel size in arcsec
read=5.0    ##readout noise 
dark=0.01  ## dark current 
sky=2300.0#http://www.eso.org/sci/facilities/eelt/science/drm/tech_data/background/, Sky brightness in K-band ([No./s/μm/m2/arcsec2])
Dist=49.97*kpc## distance of LMC
extinc= 0.2   ##Ext(K-band) Ext(V) map toward LMS taken from Dobashi et al. (2008), and A_k/Av=0.114 from Cardeli 1989 
frac= pow(10.0,0.4*extinc);       
nw=500
## This file contain detection efficiency versus wavelength in K-band from 
#https://www.eso.org/observing/etc/tmp/49a15504-1c35-4472-ad9x-5aff21fd4222//plot_eff_appletGraph.htm 
filtk=np.zeros((nw,2)) ## two columns:  wave length (nm), transmission(0-100)
filtk=np.loadtxt("./filterk.txt")
filtk[:,1]=filtk[:,1]/100.0 
################# CLASS ############################################
class expo: 
    def texp1(self, seeing,  Ndet,  snr,  Temp,  Rstar):
        psf_area=np.pi*float(2.0*seeing/pix_s)**2.0 ## number of pixel inside PSF area
        inte=0.0
        for i in range(nw):
            wave=float(filtk[i,0])*nm##meter
            dw= 0.1*nm ## meter
            E= hplanck*velocity/wave
            ff= bb*pow(wave,-5.0)/(np.exp(hplanck*velocity/(kbol*Temp*wave))-1.0)/E/frac
            inte += dw*filtk[i,1]*ff
        Nobj=inte*Rstar*Rstar*area/Dist/Dist##[Number of photon /s]      
        Nsky= float(sky*300.0*0.001*area*pix_s*pix_s)##[Nomber of photon /s/pixel]
        a= Nobj*Nobj*Ndet
        b= -snr*snr*(Nobj+Nsky*psf_area+dark*psf_area) 
        c= -snr*snr*psf_area*read*read
        if(float(b**2.0-4.0*a*c)<0.0): 
            print("Something is wrong, Delta<0.0 and no solution for texp!")
        texp1=float(-b+np.sqrt(b**2.0-4.0*a*c) )/2.0/a; 
        texp2=float(-b-np.sqrt(b**2.0-4.0*a*c) )/2.0/a; 
        return(np.max([texp1, texp2]))
    ######################################################################
    def texp2(self, seeing,  Ndet,  snr,  mag):
        psf_area=np.pi*float(2.0*seeing/pix_s)**2.0 ## number of pixel inside PSF area
        Nobj= hmbp.for_flux_in_filter("Ks", mag*u.mag, instrument="HAWKI", observatory="Paranal").value *area##[Number of photon /s] 
        Nsky= float(sky*300.0*0.001*area*pix_s*pix_s)##[Nomber of photon /s/pixel]
        a= Nobj*Nobj*Ndet
        b= -snr*snr*(Nobj+Nsky*psf_area+dark*psf_area) 
        c= -snr*snr*psf_area*read*read
        if(float(b**2.0-4.0*a*c)<0.0): 
            print("Something is wrong, Delta<0.0 and no solution for texp!")
        texp1=float(-b+np.sqrt(b**2.0-4.0*a*c) )/2.0/a; 
        texp2=float(-b-np.sqrt(b**2.0-4.0*a*c) )/2.0/a; 
        return(np.max([texp1, texp2]))
    ######################################################################













































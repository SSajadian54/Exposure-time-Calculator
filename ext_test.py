from EXPc import  expo
timeE = expo() 

## ********************* Assumptions *******************************
## In this code, the source star is a point-like object, and insie the LMC. The k-band extinction is ~0.2 mag; 
## I use a constant amount for the sky brightness in k-band as 2300 [No. photon/s/ micro meter/arcsec^2 ]  
## CCD dark current is fixed at 0.01 No./pixel/s
## CCD readout noise is fixed at  5 No./pixel, per observation
## *****************************************************************



# The first function "texp1()" determines the desired exposure time for each observation to reach the demanded "SNR" during "Ndet" observations by taking the surface temperature and radius of the target.  
# The inputs of this function are (1) seeing amount, (2) number of observatuions,  (3) demanded SNR, (4) the surface temperature, (5) radius of a point-like source star. 
##So, for calculating the exposure time you should adjust the following parameters
seeing =1.0## arcsec
Ndet=25.0  ##Number of observations 
snr=5.0    ## Signal to Noise Ratio
Temp= 15000.0## surface temperature of target [K]
Rstar=1.8*696340000.0 ## stellar radius [K]
print("The exposure time(s) should be:  " ,   timeE.texp1(seeing,  Ndet,  snr,  Temp,  Rstar) )



# The second function "texp2()" determines the desired exposure time for each observation to reach the demanded "SNR" during "Ndet" observations by taking the apparent magnitude of the target in the Ks-band. The code uses "HowManyPhotons" (https://pypi.org/project/HowManyPhotons/) python module well developed by K. Leschinski to calculate the numebr of photon per second  
# The inputs of this function are (1) seeing amount, (2) number of observatuions,  (3) demanded SNR, (4) Ks-band apparent magnitude of target
##So, for calculating the exposure time you should adjust the following parameters
seeing =1.0   ## arcsec
Ndet=   25.0  ##Number of observations 
snr=    5.0   ## Signal to Noise Ratio
mag=    20.5  ## Ks-band apparent magnitude
print("Exposure time(s) should be:    " ,  timeE.texp2(seeing,  Ndet,  snr, mag))









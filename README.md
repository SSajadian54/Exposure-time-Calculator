# Exposure-time-Calculator


There are two simple codes that both calculate the desired exposure time for each observation to reach the demanded "SNR" during "Ndet" observations.

texp1() takes (1) the seeing amount, (2) the number of observations, (3) demanded SNR, (4) the surface temperature, and (5) the radius of a point-like source star. 

texp2() takes (1) seeing amount, (2) number of observations, (3) demanded SNR, (4) Ks-band apparent magnitude of target. This function uses the "HowManyPhotons" (https://pypi.org/project/HowManyPhotons/) python module well developed by K. Leschinski to calculate the number of photons per second for a given apparent magnitude.  

A simple python code ("ext_test.py") to call these functions is made as well.   

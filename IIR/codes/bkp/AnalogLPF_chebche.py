import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
from scipy import signal

#Band pass Filter Specification

#sampling rate
Fs=48000      

# 1. Tolerance
d=0.15      

# 2. passband Range
j=114         #filter number
Fp2=(3+0.6*(j-109))*1000   
Fp1=(3+0.6*(j-107))*1000

#normalized pass band frequencies
wp1=2* np.pi * (Fp1/Fs)
wp2=2* np.pi * (Fp2/Fs)
wc=(wp1+wp2) /2    #Center Frequency

# 3. stopband
df=0.3*1000     #Transition Band
Fs1=Fp1+df
Fs2=Fp2-df

#normalized stop band frequencies
ws1=2* np.pi * (Fs1/Fs)
ws2=2* np.pi * (Fs2/Fs)

# bilinear transform relation
ap1=np.tan(wp1/2)  
ap2=np.tan(wp2/2)
as1=np.tan(ws1/2)
as2=np.tan(ws2/2)

# THE ANALOG LOW PASS FILTER

# 1.Low pass Filter Specifications
ao=np.sqrt(ap1*ap2)
B=ap1-ap2
alp=1
als1=(as1**2 -ao**2) / (B*as1)
als2=(as2**2 -ao**2) / (B*as2)
als=np.minimum(abs(als1),abs(als2))

# 2. Low Pass Chebyshev filter parameters
D1=(1/(1-d)**2)-1
D2=(1/(d**2))-1
cn=np.cosh(4*np.arccosh(als))
R1=np.sqrt(D2) / cn  #Min Range
R2=np.sqrt(D1)       #Max Range
print R1,"<= e <=",R2
N=int(math.ceil((np.arccosh(np.sqrt(D2/D1))) / np.arccosh(als)))
print "N>=",N    # order of the filter

e=np.round(np.linspace(R1,R2,6),2)
e_2=e**2  
h1=np.zeros((1,200))
Omga_L=np.linspace(0,2,200)
for i in range(6):
    h1[0]=np.sqrt(1/(1+e_2[i]*((8*(Omga_L**4)-8*(Omga_L**2)+1)**2)))
    plt.plot(Omga_L,h1[0],label=e[i])
plt.xlabel('$Frequency$')
plt.ylabel('$Magnitude$')
plt.legend()
plt.grid()
plt.show()

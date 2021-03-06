import numpy as np
import matplotlib.pyplot as plt
import math


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

e=0.37
e_2=e**2

w_bp=np.linspace(-0.4,0.4,200)
s=(1-np.exp(-1j*w_bp*np.pi))/(1+np.exp(-1j*w_bp*np.pi))
Omga_o=0.4594
BW=0.0953
s_L=(((s)**2)+Omga_o**2)/(BW*s)

h_design=(0.3125)/(((s_L)**4)+(1.1068*(s_L)**3)+(1.6125*(s_L)**2)+(0.9140*s_L)+0.3366)

plt.plot(w_bp,abs(h_design),label='design')

plt.xlabel('$Frequency$')
plt.ylabel('$Magnitude$')
plt.legend()
plt.grid()
plt.show()

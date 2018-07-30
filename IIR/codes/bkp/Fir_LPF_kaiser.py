import numpy as np
import matplotlib.pyplot as plt
import mpmath
import math
import scipy.special as sp
from scipy import signal


Fs=48000      #sampling rate

#2.1 THE DIGITAL FILTER

# 1. Tolerance
d=0.15      

# 2. passband Range
j=114         #filter number
Fp2=(3+0.6*(j-109))*1000   
Fp1=(3+0.6*(j-107))*1000

#Unnormalized discrete time filter pass band frequencies

wp1=2* np.pi * (Fp1/Fs)
wp2=2* np.pi * (Fp2/Fs)

wl=(wp1-wp2)/2

df=0.3*1000		   #Transition Band

dw=2*np.pi*(df/Fs)

#kaiser window

A=-20*np.log10(d)

N=math.ceil((A-8)/(4.57*dw))
N=100 # assume N=100

if(A>50):
    betaN=0.1102*(A-8.7)
elif(21<=A<=50):
    betaN=0.5849*((A-21)**(0.4))+0.07886*(A-21)
else:
    betaN=0

M=int(2*N-2)    
n=np.linspace(-N,N,M)
w_n=np.zeros([M,])

for i in range(M):
    w_n[i]=float(mpmath.besseli(0,betaN*np.sqrt(1-(n[i]/N)**2)))/float(mpmath.besseli(0,betaN))

h_lp=(np.sin(n*wl)/(n*np.pi))*w_n

H_abs=np.fft.fftshift(np.abs(np.fft.fft(h_lp)))

plt.plot(H_abs)
plt.xlabel('$Frequency$')
plt.ylabel('$Magnitude$')

plt.grid()
plt.show()

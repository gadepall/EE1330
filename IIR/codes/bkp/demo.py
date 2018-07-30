import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from N_epsilon import parameters
from Gen_LPF_Coeff import filt_design

#Passband Cutoffs
Fp2=6.0
Fp1=7.2

#Transition Band
df=0.3

#Passband && stopband tolerance
d=0.15

#sampling rate
Fs=48

N,R1,R2,alp = parameters(Fp2,Fp1,df,d,Fs)


e=0.6197

b,a=filt_design(N,e,alp)

print b,a

w, h = signal.freqs(b, a)
plt.plot(w, abs(h))
#plt.xscale('log')
plt.title('Chebyshev Type I frequency response (rp=5)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.axvline(alp, color='green') # passband frequency
plt.axhline(1-d, color='green') # rp

plt.grid()
plt.show()

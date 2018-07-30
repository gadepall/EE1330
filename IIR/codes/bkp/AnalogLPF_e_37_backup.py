import numpy as np
import matplotlib.pyplot as plt
import math

from N_epsilon import parameters

#Passband Cutoffs
Fp2=6.0
Fp1=7.2

#Transition Band
df=0.3

#Passband && stopband tolerance
d=0.15

#sampling rate
Fs=48

N,R1,R2,ao,B = parameters(Fp2,Fp1,df,d,Fs)

e=0.37
e_2=e**2

Omga_L=np.linspace(0,2,200)
s=1j*Omga_L

h_spec=np.sqrt(1/(1+e_2*((8*(Omga_L**4)-8*(Omga_L**2)+1)**2)))
h_design=(0.3125)/(((s)**4)+(1.1068*(s)**3)+(1.6125*(s)**2)+(0.9140*s)+0.3366)
plt.plot(Omga_L,h_spec,label='specifications')
plt.plot(Omga_L,abs(h_design),'o',label='design')
plt.xlabel('$Frequency$')
plt.ylabel('$Magnitude$')
plt.legend()
plt.grid()
plt.show()

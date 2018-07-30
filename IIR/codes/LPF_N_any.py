import numpy as np
import matplotlib.pyplot as plt


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

e_array=np.linspace(R1,R2,6)

Omga_L=np.linspace(0,2,200)

s=1j*Omga_L

for e in e_array:
	b,a=filt_design(N,e,alp)
	
	H_lp=np.polyval(b,s)/np.polyval(a,s)

	plt.plot(Omga_L,abs(H_lp),label=round(e,2))

plt.xlabel('$Frequency(\Omega)$')
plt.ylabel('$|H_{lp}(j\Omega)|$')
plt.title('Magnitude response of LPF for different values of $\epsilon$')
plt.legend()
plt.grid()
plt.show()

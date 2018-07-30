import numpy as np
import matplotlib.pyplot as plt

from N_epsilon import parameters
from LPF_design import filt_design

#Passband Cutoffs
Fp2=6.0
Fp1=7.2

#Transition Band
df=0.3

#Passband && stopband tolerance
d=0.15

#sampling rate
Fs=48

N,R1,R2,ao,B,alp,als,ap1,ap2,as1,as2 = parameters(Fp2,Fp1,df,d,Fs)


e=0.6197

 
Omga_bp=np.linspace(-0.8,0.8,200)
s=1j*Omga_bp

s_L=(((s)**2)+ao**2)/(B*(s))

H_bp=filt_design(N,e,alp,s_L)

s1=np.array([1j*ap1,1j*ap2,1j*as1,1j*as2])

s1_L=(((s1)**2)+ao**2)/(B*(s1))

H_point=filt_design(N,e,alp,s1_L)

H_bp=np.array(H_bp)

print abs(s1)
print abs(np.array(H_point))

pt=[5,-80,5,-80]
for i in range(len(s1)):
	A=[np.around(abs(s1[i]),decimals=4)]
	B=[np.around(abs(H_point[i]),decimals=2)]
	plt.plot(A,B,'o')

	for xy in zip(A,B):
		plt.annotate('(%s,%s)'%xy,xy=xy,xytext=(pt[i],1),textcoords='offset points')
plt.plot(Omga_bp,abs(H_bp),'b',label='design')
plt.xlabel('$Frequency(\Omega)$')
plt.ylabel('$|H_{bp}(j\Omega)|$')
plt.title('Magnitude response of analog BPF for $\epsilon$=0.6197')
plt.axis([-1.5,1.5,0,1.2])
plt.legend(loc='lower left')
plt.grid()
plt.show()

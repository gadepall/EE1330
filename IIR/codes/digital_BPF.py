import numpy as np
import matplotlib.pyplot as plt
import math

from F_omega import f_Omega
from Omegabp_Omegalp import Omega_blp
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

def W(Fs,F):
    w=2*float(F)/Fs
    return w

ap1,ap2,as1,as2=f_Omega(Fp1,Fp2,df,Fs)
ao,B,alp,als = Omega_blp(ap1,ap2,as1,as2)

N=4
e=0.6197

w_bp=np.linspace(-0.5,0.5,200)

s=(1-np.exp(-1j*w_bp*np.pi))/(1+np.exp(-1j*w_bp*np.pi))

s_L=(((s)**2)+ao**2)/(B*s)

H_bp=filt_design(N,e,alp,s_L)	

wp1=W(Fs,Fp1)
wp2=W(Fs,Fp2)
ws1=W(Fs,Fp1+df)
ws2=W(Fs,Fp2-df)

w_point=np.array([wp1,wp2,ws1,ws2])

s1=(1-np.exp(-1j*w_point*np.pi))/(1+np.exp(-1j*w_point*np.pi))

s1_L=(((s1)**2)+ao**2)/(B*(s1))

H_point=filt_design(N,e,alp,s1_L)

H_bp=np.array(H_bp)

pt=[1,-80,1,-80]
for i in range(len(s1)):
	A=[np.around(w_point[i],decimals=4)]
	B=[np.around(abs(H_point[i]),decimals=2)]
	plt.plot(A,B,'o')

	for xy in zip(A,B):
		plt.annotate('(%s,%s)'%xy,xy=xy,xytext=(pt[i],1),textcoords='offset points')

plt.plot(w_bp,abs(H_bp),'b',label='design')
plt.xlabel('$Frequency(\omega/\pi)$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.title('Magnitude response of digital BPF for $\epsilon$=0.6197')
plt.axis([-1,1,0,1])
plt.legend()
plt.grid()
plt.show()

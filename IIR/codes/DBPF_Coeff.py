import numpy as np
import matplotlib.pyplot as plt

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

wp1=W(Fs,Fp1)
wp2=W(Fs,Fp2)
ws1=W(Fs,Fp1+df)
ws2=W(Fs,Fp2-df)

N=4
b1=np.loadtxt('Numerator_ABPF')
a1=np.loadtxt('Denominator_ABPF')



a2=0
for i in range(2*N+1):
	coeff1=a1[i]*np.poly1d([1,1])**i
	poly_denom1=np.poly1d([-1,1])**(2*N-i)
	a2=a2+poly_denom1*coeff1
b2=(np.poly1d([-1,1])**N)*(np.poly1d([1,1])**N)*b1[0]

np.savetxt('Numerator_DPBF',np.array(b2))
np.savetxt('Denominator_DBPF',np.array(a2))

w_bp=np.linspace(-0.5,0.5,200)

z_inv=np.exp(-1j*w_bp*np.pi)

H_bp=np.polyval(b2,z_inv)/np.polyval(a2,z_inv)

w_point=np.array([wp1,wp2,ws1,ws2])

z_inv1=np.exp(-1j*w_point*np.pi)

H_point=np.polyval(b2,z_inv1)/np.polyval(a2,z_inv1)


pt=[1,-80,1,-80]
for i in range(len(w_point)):
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

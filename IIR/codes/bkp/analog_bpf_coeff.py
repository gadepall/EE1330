import numpy as np
import matplotlib.pyplot as plt
from F_omega import f_Omega

ap1,ap2,as1,as2=f_Omega(Fp1,Fp2,df,Fs)
#np.savetxt('Numerator_ABPF',np.array(b1))
#np.savetxt('Denominator_ABPF',np.array(a1))
b1=np.loadtxt('Numerator_ABPF')
a1=np.loadtxt('Denominator_ABPF')
print b1,a1
Omga_bp=np.linspace(-1,1,200)
s=1j*Omga_bp

H_bp=np.polyval(b1,s)/np.polyval(a1,s)

s1=np.array([1j*ap1,1j*ap2,1j*as1,1j*as2])
H_point=np.polyval(b1,s1)/np.polyval(a1,s1)

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

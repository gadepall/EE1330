import numpy as np
import math

from F_omega import f_Omega
from Omegabp_Omegalp import Omega_blp

def parameters(Fp2,Fp1,df,d,Fs):
	
	ap1,ap2,as1,as2=f_Omega(Fp1,Fp2,df,Fs)
	
	ao,B,alp,als=Omega_blp(ap1,ap2,as1,as2)
	
	#  Low Pass Chebyshev filter parameters
	D1=(1/(1-d)**2)-1
	D2=(1/(d**2))-1
	cn=np.cosh(4*np.arccosh(als))
	R1=np.sqrt(D2) / cn  #Min Range
	R2=np.sqrt(D1)       #Max Range

	N=int(math.ceil((np.arccosh(np.sqrt(D2/D1))) / np.arccosh(als)))

	return N,R1,R2,alp


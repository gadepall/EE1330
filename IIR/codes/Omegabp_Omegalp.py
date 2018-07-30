import numpy as np
def Omega_blp(ap1,ap2,as1,as2):
	
	# 1.Low pass Filter Specifications
	ao=np.sqrt(ap1*ap2)
	B=ap1-ap2
	alp=(ap1**2 - ao**2) /(B*ap1)
	als1=(as1**2 - ao**2) / (B*as1)
	als2=(as2**2 - ao**2) / (B*as2)
	als=np.minimum(abs(als1),abs(als2))
	return ao,B,alp,als

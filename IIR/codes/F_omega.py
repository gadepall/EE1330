import numpy as np
def f_Omega(Fp1,Fp2,df,Fs):
	def F_w(F_s,F):
		w = 2*np.pi*float(F)/F_s
		ap=np.tan(w/2.0)
		return ap

	#passband Omega cutoffs
	ap1=F_w(Fs,Fp1)
	ap2=F_w(Fs,Fp2)

	#stopband Omega cutoffs
	as1=F_w(Fs,Fp1+df)
	as2=F_w(Fs,Fp2-df)

	return ap1,ap2,as1,as2

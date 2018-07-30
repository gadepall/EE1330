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

N,R1,R2,ao,B,alp,als = parameters(Fp2,Fp1,df,d,Fs)

print R1,"<= e <=",R2

print "N>=",N    # order of the filter

import numpy as np

def filt_design(N,e,alp,s):
    yN= (1/2.0)*((np.sqrt(1+(1/e**2))+(1/e))**(1/N)-(np.sqrt(1+(1/e**2))+(1/e))**(-1/N))
    C0=yN
    C=[]
    b=[]
    for k in range(1,(N/2)+1):
    	C.append(yN**2+np.cos((2*k-1)*np.pi/(2.0*N))**2)
    	b.append(2*yN*np.sin((2*k-1)*np.pi/(2.0*N)))
    
    def par(i,C,b):
        tot_ck=1
        pole_sum=1
        for k in range(N/2):
            tot_ck=tot_ck*C[k]
            pole_sum=pole_sum*(i**2+b[k]*alp*i+C[k]*(alp**2))
        return tot_ck,pole_sum
    H=[]
    if(N%2 == 0):
        for i in s:
            tot_ck,pole_sum=par(i,C,b)
            H.append((alp**N)*tot_ck*np.sqrt(1/(1+e**2))/pole_sum)
    else:
        for i in s:
            tot_ck,pole_sum=par(i,C,b)
            H.append(((alp**N)*tot_ck*C0)/(pole_sum*(i+alp*C0)))
    return H

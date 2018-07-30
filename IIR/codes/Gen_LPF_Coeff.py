import numpy as np

def filt_design(N,e,alp):
    yN= (1/2.0)*((np.sqrt(1+(1/e**2))+(1/e))**(1/N)-(np.sqrt(1+(1/e**2))+(1/e))**(-1/N))
    C0=yN
    C=[]
    b=[]
    for k in range(1,(N/2)+1):
    	C.append(yN**2+np.cos((2*k-1)*np.pi/(2.0*N))**2)
    	b.append(2*yN*np.sin((2*k-1)*np.pi/(2.0*N)))
    
    
    tot_ck=1
    pole_sum=1
    if(N%2==0):
		for k in range(N/2):
			tot_ck=tot_ck*C[k]
			pole_sum=pole_sum*np.poly1d([1,b[k]*alp,C[k]*(alp**2)])
		tot_ck=np.poly1d([0,1])*(alp**N)*tot_ck*np.sqrt(1/(1+e**2))
		#pole_sum=np.array(pole_sum)
    else:
		for k in range(N/2):
			tot_ck=tot_ck*C[k]
			pole_sum=pole_sum*np.poly1d([1,b[k]*alp,C[k]*(alp**2)])
		tot_ck=np.poly1d([0,1])*(alp**N)*tot_ck*C0
		pole_sum=pole_sum*np.poly1d([1,alp*C0])
  
    return tot_ck,pole_sum

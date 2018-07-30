import numpy as np
import matplotlib.pyplot as plt
import math

from N_epsilon import parameters

N=4

alp=1.0

e=0.37
e_2=e**2

Omga_L=np.linspace(0,2,200)
s=1j*Omga_L

def h_point(a):
	s=1j*a
	h=(0.3125)/(((s)**4)+(1.1068*(s)**3)+(1.6125*(s)**2)+(0.9140*s)+0.3366)
	return h
h_spec=np.sqrt(1/(1+e_2*((8*(Omga_L**4)-8*(Omga_L**2)+1)**2)))
h_design=(0.3125)/(((s)**4)+(1.1068*(s)**3)+(1.6125*(s)**2)+(0.9140*s)+0.3366)
plt.plot(Omga_L,h_spec,label='specifications')
plt.plot(Omga_L,abs(h_design),'o',label='design')
plt.plot([alp,alp],[0,abs(h_point(alp))] , color=(1,0,0),marker='o',label="H_alp" )
plt.xlabel('$Frequency$')
plt.ylabel('$Magnitude$')
plt.legend()
plt.grid()
plt.show()

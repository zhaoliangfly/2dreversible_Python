import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

KT = 8.31*0.3
Eps_0 = 0.7
a_0 = 1.0
N = 1400.0
L_P = 40
L_Q = 40

def Jiecheng(n):
	return 0.5*np.log(2.0*np.pi*n)+n*np.log(n)-n;

def G_gas(N, L_A, L_P, L_Q):
	c_up = N-(L_A/a_0)*(L_A/a_0)
	c_down = (L_P/a_0)*(L_Q/a_0)-((L_A/a_0)+2.0)*((L_A/a_0)+2.0)
	return -KT*(Jiecheng(c_down)-Jiecheng(c_up)-Jiecheng(c_down-c_up))

def G_cluster(L_A, a_0, Eps_0):
	return Eps_0*(L_A+L_A)/a_0-2.0*Eps_0*(L_A/a_0)*(L_A/a_0)

def G(L_A, a_0, Eps_0, N, L_P, L_Q):
	return (G_cluster(L_A, a_0, Eps_0)+G_gas(N, L_A, L_P, L_Q))/KT

def G_adjust(L_A, a_0, Eps_0, N, L_P, L_Q):
	return G(L_A, a_0, Eps_0, N, L_P, L_Q)-G(1.0, a_0, Eps_0, N, L_P, L_Q)

g_1=[]
g_2=[]
g_3=[]
g_4=[]
x_square=[]
x=np.arange(1,np.sqrt(N)-0.1,0.1)
for i in x:
	x_square.append(i*i)
	g_1.append(G_adjust(i, a_0, Eps_0, N, L_P, L_Q))
	#g_2.append(G_adjust(i, a_0, Eps_0, N, L_P, L_Q))
	#g_3.append(G_adjust(i, a_0, Eps_0, N, L_P, L_Q))
	#g_4.append(G_adjust(i, a_0, Eps_0, N, L_P, L_Q))

#plt.plot(x_square,g_1,"r-",x_square,g_2,"b-",x_square,g_3,"y-",x_square,g_4,"g-")
plt.plot(x_square,g_1,"g-")
plt.show()


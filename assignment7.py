import numpy as np

def belmf(x,a,b,c):
	return 1.0/(1.0 + np.abs((x-c)/a)**(2*b))



print("Enter the age (x): ",end="")
x=int(input())

m_young = belmf(x,20,2,0)
m_old = belmf(x,30,3,100)

print("1. More or less young: ",round(m_young**(0.5),2))
print("2. Not young and not old: ",round(min(1-m_young,1-m_old),2))
print("3. Young but not too young: ",round(min(m_young,(1-(m_young**2))),2))
print("4. Extremely old: ",round(m_old**4,2))



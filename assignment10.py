def trap_mf(x,a,b,c,d):
	
	if(x<a or x>d):
    		mem = 0
	elif(x>=a and x<=b):
    		mem = float(x-a)/float(b-a)
	elif(x>=c and x<=d):
    		mem = float(d-x)/float(d-c)
	else:
    		mem = 1
	return mem

print("Enter value of Blood Pressure: ",end="")
Inp_1 = int(float(input()))

print("Enter value of Temperature: ",end="")
Inp_2 = int(float(input()))

bp_h = trap_mf(Inp_1, 90,105,115,115)
bp_n = trap_mf(Inp_1, 60,75,85,100)
bp_l = trap_mf(Inp_1, 40,40,55,65)

t_h = trap_mf(Inp_2,100,104,110,110)
t_l = trap_mf(Inp_2,90,90,94,97)
t_n = trap_mf(Inp_2,96,98,99,102)

health = ["Poor", "Normal", "Good"]

if(bp_n >=0.7 and t_n>=0.7):
    print("Health is ",health[2])
elif(bp_n <=0.7 and t_n>=0.7):
    print("Health is ",health[1])
elif(bp_n >=0.7 and t_n<=0.7):
    print("Health is ",health[1])
elif(bp_n <0.7 and t_n<0.7):
    print("Health is ",health[0])
else:
    print("Prediction of health is critical")
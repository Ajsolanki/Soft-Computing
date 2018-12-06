import matplotlib.pyplot as p
print("Enter the value of a,b,c,d")
inp = input()

a=int(inp.split(" ")[0])
b=int(inp.split(" ")[1])
c=int(inp.split(" ")[2])
d=int(inp.split(" ")[3])

x_c = [a,b,c,d]
y_c = [0,1,1,0]

p.plot(x_c,y_c)
p.show()

print("Enter the value of x :")
x=float(input())

if(x<a or x>d):
    mem = 0

elif(x>=a and x<=b):
    mem = float(x-a)/float(b-a)

elif(x>=c and x<=d):
    mem = float(d-x)/float(d-c)

else:
    mem = 1

print("Its membership function is ",mem)

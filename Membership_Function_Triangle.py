import matplotlib.pyplot as plt

print("Enter the value of a,b :")
x=input()
a=int(x.split(" ")[0])
b=int(x.split(" ")[1])
m=(a+b)/2

x_c = [a,m,b]
y_c = [0,1,0]

plt.plot(x_c,y_c)
plt.show()


print("Enter the value of x")
y=float(input())

if(y<=a):
    mem = 0
elif(y>a and y<=m):
    mem = float(y-a)/float(m-a)

elif(y>m and y<b):
    mem = float(b-y)/float(b-m)

else:
    mem = 0

print("Its membership function is ",mem)




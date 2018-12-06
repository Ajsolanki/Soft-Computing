import random as rd
n = int(input("Enter the number of N-queen Problem: "))

list = []
for i in range(1,n+1):
    list.append(i)


temp = rd.sample(list, n)
print("Encoding of N-Queen Problem",temp)
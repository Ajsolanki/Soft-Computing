#Centroid of Area
dict = {0:0.1, 0.1:0.1, 0.2:0.1, 0.3:0.2, 0.4:0.2, 0.5:0.2, 0.6:0.2, 0.7:0.5, 0.8:0.5, 0.9:0.5, 1.0:0.5}
cent = 0

sum_xi_wi = 0
sum_wi = 0

for i in dict:
    sum_wi += dict[i]
    sum_xi_wi += i*dict[i]

cent = sum_xi_wi/sum_wi

print("Centroid is:",cent)

#Smallest of Maximum and Largest of Maximum
dict = {0:0.1, 0.1:0.1, 0.2:1, 0.3:0.2, 0.4:0.8, 0.5:0.2, 0.6:1, 0.7:0.5, 0.8:1, 0.9:0.5, 1.0:0.1}
sum_of_max = 0
list_of_max = []
count = 0

for i in dict:
    if(dict[i]==1 or dict[i]==1.0):
        list_of_max.append(i)
        sum_of_max += i
        count += 1

mean_of_max = sum_of_max/count    
print("Mean of Maximum : ",mean_of_max)

small_of_max = min(list_of_max)
larg_of_max = max(list_of_max)

print("Smallest of Maximum :", small_of_max)
print("Largest of Maximum: ",larg_of_max)


#Bi-Sector of Area
list_of_mem = []

for i in dict:
    list_of_mem.append(dict[i])

print("Bisector of Area: ", sum(list_of_mem)/len(list_of_mem))
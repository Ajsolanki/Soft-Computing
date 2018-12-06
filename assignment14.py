#Dataset  item in  ("item_name", Weight, Cost)
dataset = [('a',10,100),('b',5,200),('c',15,150),('d',12,80),('e',18,180),('f',14,150),('g',8,120)]

import random as rd

temp  = [rd.choice([0,1]) for i in range(len(dataset))]
K = 50
def fitness(chromosome):
    sum_weight,sum_cost = 0,0
    for i in range(len(chromosome)):
        if temp[i]==1:
            sum_weight += dataset[i][1]
            sum_cost += dataset[i][2]
    return sum_weight,sum_cost        

print("Binary Encoding of Parent:", temp)
print("Total weight and Total Cost :",fitness(temp))
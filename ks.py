import random

def input_from_user():
    K = int(input("Enter Size of bag in kg: "))
    N = int(input("Enter total number of items:"))
    items = {}
    for i in range(N):
        weight = input("Enter the weight of item"+str(i+1)+":")
        cost = input("Enter the cost of item"+str(i+1)+":")
        items[i+1] = (weight,cost)
    return items, K

#items, K = input_from_user()
K = 50
items = {1:(25,45),2:(20,40),3:(60,92),4:(12,9)}


def gen_parents(L):
    pos_val =[0,1]
    p1 = []
    p2 = []
    for i in range(L):
        p1.append(random.choice(pos_val))    
        p2.append(random.choice(pos_val))
    return p1,p2

p1,p2 = gen_parents(len(items))

def fitness(parent, items, K):
    cost = 0
    weight = 0
    for i in range(len(parent)):
        if parent[i]==1:
            weight += items[i+1][0]
            cost += items[i+1][1]
    qualify = bool
    if weight <= K:
        qualify = True
    else:
        qualify = False
    
    return cost,weight, qualify

def crossover(p1,p2):
    p3 = []
    for i in range(len(p1)):
        res = p1[i] or p2[i]
        p3.append(res)
    return p3
        
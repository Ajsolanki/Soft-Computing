import random as r
X= [1, 2, 3]
Y= ['a','b','c','d']
Z = ['one', 'two']
def make_matrix(m,n):
    mat = []
    for i in range(m):
        mat.append([])
        for _ in range(n):
            mat[i].append(round(r.random(),2))
    return mat

R1 = make_matrix(3,4)
R2 = make_matrix(4,2)

def max_min_composition(x,y):
    min1 = []
    t1 = R1[x]
    t2 = [i[1] for i in R2]
    for k in range(len(t1)):
        min1.append(min(t1[k],t2[k]))      
    return max(min1)

def max_product(x,y):
    min2 = []
    t1 = R1[x]
    t2 = [i[1] for i in R2]
    for k in range(len(t1)):
        min2.append(t1[k]*t2[k])
    return max(min2)

print("Max-min Composition is:",max_min_composition(2,1))
print("Max-Product Composition is:",round(max_product(2,1),2))
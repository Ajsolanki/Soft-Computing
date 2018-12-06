Matrix_A = {'a':[0.1,0.2,0.3],'b':[0.4,0.5,0.6],'c':[0.7,0.8,0.9]}
Matrix_B = {1:[1,0.2,0.6],2:[0.3,0.5,1],3:[0.7,0.8,0.1]}

def min_max(Matrix_A,Matrix_B,i,j):
    g_min = 1
    g_max = 0
    for k in range(len(Matrix_A[i])):
        g_max = max(Matrix_A[i][k],Matrix_B[j][k])
        if g_max<g_min:
            g_min = g_max
    return g_min

def max_prod(Matrix_A,Matrix_B,i,j):
    g_max = 0
    g_prod = 1
    for k in range(len(Matrix_A[i])):
        g_prod = Matrix_A[i][k] * Matrix_B[j][k]
        if g_max<g_prod:
            g_max = g_prod
    return g_max

print("Max-product Composition for a and 2 :",max_prod(Matrix_A,Matrix_B,"a",2))
print("Min-max Composition for b and 3 :",min_max(Matrix_A,Matrix_B,"b",3))
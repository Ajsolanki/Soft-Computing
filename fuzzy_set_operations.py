A = { 1:0.8 , 2:0.7 , 3:0.1 , 4:0.1 , 5:1, 6:0.2}
B = { 1:0.1 , 2:0.8 , 3:0.5 , 4:0.2 , 5:0 , 6:0}

def core(X):
    for i in range(1,len(X)+1):
        if(X[i]==1):
            print("Core is : ",i)

def height(X):
    max = X[1]
    for i in X:
        if(X[i] > max):
            max = X[i] 
    print("Height is",max)

def support(X):
    for i in X:
        if(X[i] > 0):
            print("Support is ",i," whose membership value is ",X[i])

def crossover(X):
    for i in X:
        if(X[i] == 0.5):
            print("Crossover values ",i)

def sum(X,Y):
    S = { 1:0 , 2:0 , 3:0 , 4:0 , 5:0 , 6:0 }

    for i in range(1,7):    
        S[i] = round(((X[i] + Y[i]) - X[i]*Y[i]),1)
    print(S)
    

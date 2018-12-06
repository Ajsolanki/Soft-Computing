#!/usr/bin/python3

def check(r1,r2):
    flag=False
    if r1.shape[1]==r2.shape[0]:
        flag=True
    if r1.shape[0]==r2.shape[1]:
        t=r2
        r2=r1
        r1=t
        flag=True
    return flag

def max_min(r1,r2):
    if check(r1,r2):
        r=[]
        for i in range(r1.shape[0]):
            for j in range(r1.shape[1]):
                l=[]
                for k in range(r2.shape[0]):
                    l.append(min(r1[i,k],r2[k,j]))
            r.append(max(l))
    else:
        r='Invalid input.'
    return r

def max_prod(r1,r2):
    if check(r1,r2):
        r=[]
        for i in range(r1.shape[0]):
            for j in range(r1.shape[1]):
                l=[]
                for k in range(r2.shape[0]):
                    l.append(r1[i,k]*r2[k,j])
            r.append(max(l))
    else:
        r='Invalid input.'
    return r

#%%

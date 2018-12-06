#!/usr/bin/python3


import numpy as np

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary
    '''
    ind={}
    for i,j in d.items():
        if j in ind:
            ind[j].append(i)
        else:
            ind[j]=[i]
    for i in ind:
        ind[i].sort()
    return ind

def smallest_of_max(T):
    lis=[]
    m=list(T.values())
    n=list(T.keys())
    for i in range(len(m)):
        if m[i]==1.0 or m[i]==1:
            lis.append(n[i])
    return min(lis)

def largest_of_max(T):
    lis=[]
    m=list(T.values())
    n=list(T.keys())
    for i in range(len(m)):
        if m[i]==1.0 or m[i]==1:
            lis.append(n[i])
    return max(lis)

def mean_of_max(T):
    lis=[]
    m=list(T.values())
    n=list(T.keys())
    for i in range(len(m)):
        if m[i]==1.0 or m[i]==1:
            lis.append(n[i])
    return np.mean(lis)

def centroid_of_area(T):
    d=dict_invert(T)
    num=0
    den=0
    for i in list(d.keys()):
        num=num+np.sum(d[i])*i
        den=den+len(d[i])*i
    return num/den

def bisector_of_area(T,eps=0.2):
    l=list(T.keys())
    for i in range(len(l)):
        if np.abs(np.sum(list(T.values())[:i])-np.sum(list(T.values())[i:]))<=eps:
            c=l[i]
    return c
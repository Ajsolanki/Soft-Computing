#!/usr/bin/python3

def ath(T,H):
    temp=[]
    humi=[]
    h=list(H.keys())
    hv=list(H.values())
    t=list(T.keys())
    tv=list(T.values())
    for i in range(len(t)):
        if tv[i]>=0.8:
            temp.append(t[i])
    for j in range(len(h)):
        if hv[j]>=0.8:
            humi.append(h[j])
    res=[]
    for i in temp:
        for j in humi:
            res.append(('Temprature:'+str(i),'Humidity:'+str(j)))
    return res

T={16:0.4,18:0.8,20:1,22:1,24:0.8,26:0.5}
H={0:0.2,20:0.8,40:1,60:0.6,80:0.2}

ath(T,H)    
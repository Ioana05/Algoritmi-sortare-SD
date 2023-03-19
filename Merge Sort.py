def interclasare(v,st,dr,mijl):
    i=st
    j=mijl+1
    aux=[]
    while i<=mijl and j<=dr:
        if v[i]<=v[j]:
            aux.append(v[i])
            i+=1
        else:
            aux.append(v[j])
            j+=1
    aux.extend(v[i:mijl+1])
    aux.extend(v[j:dr+1])

    v[st:dr+1]=aux[:]

def Divide(v,st,dr):
    if st<dr:
        mijl=(st+dr)//2
        Divide(v,st,mijl)
        Divide(v,mijl+1,dr)
        interclasare(v,st,dr,mijl)

v=[1,7,3,2,9,15,12,11]
Divide(v,0,7)
print(v)

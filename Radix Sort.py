def RadixSort(v,n):
    #aflam numarul maxim din vector
    maxi=max(v)
    position=1
    while (maxi//position)>0:
        CountingSort(v,n,position)
        position=position*10
    return v
def CountingSort(v,n,position):
    aux = [0] * (10)  # initializam cu 0 toate elementele vectorului de frecventa
    b= [0]* (10)

    for i in range(n):
        aux[(v[i]//position)%10] += 1  # calculam frecventele elementelor din vector

    for i in range(1,10):
        aux[i]=aux[i]+aux[i-1]
    for i in range(n-1,-1,-1):
        aux[(v[i] // position) % 10]-=1
        b[aux[(v[i]//position)%10]]=v[i]
    for i in range(n):
        v[i]=b[i]
    return v

v=[9, 1, 34, 20, 15, 0, 7]
n=7
print(RadixSort(v,n))

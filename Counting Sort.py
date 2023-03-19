def counting_sort(v,aux,sorted,n):
    sorted=[]
    k=max(v) #calculam maximul din vector

    aux=[0]*(k+1) #initializam cu 0 toate elementele vectorului de frecventa
    
    for i in range(n):
        aux[v[i]]+=1     #calculam frecventele elementelor din vector

    #parcurgem vectorul de frecventa si adaugam in noul vector elementele in ordine
    j=0
    for i in range(k+1):
        aparitii=aux[i]
        while(aparitii!=0):
            sorted.append(i)
            j+=1
            aparitii-=1
    return sorted


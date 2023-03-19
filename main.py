import random
import time

#COUNTING SORT

def call_counting_sort(v):
    n=len(v)
    if n<=100000000:
        return counting_sort(v,n)
    else :
        print( "Sorry, I can't handle it." )
        return
def counting_sort(v,n):

    k = max(v)  # calculam maximul din vector

    aux = [0] * (k + 1)  # initializam cu 0 toate elementele vectorului de frecventa
    sorted=[]

    for i in range(n):
        aux[v[i]] += 1  # calculam frecventele elementelor din vector

    # parcurgem vectorul de frecventa si adaugam in noul vector elementele in ordine
    j = 0
    for i in range(k + 1):
        aparitii = aux[i]
        while (aparitii != 0):
            sorted.append(i)
            j += 1
            aparitii -= 1
    return sorted

#MERGE SORT

def call_interclasare(v):
    st=0
    dr=len(v)-1
    return Divide(v,st,dr)
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

#QUICK SORT

def call_QuickSort(v):
    start=0
    end=len(v)-1
    return QuickSort(v,start,end)

def QuickSort( v,start,end):
    if start<end:
        index=sortingAlgorithm(v,start,end);
        QuickSort(v,start,index-1)
        QuickSort(v,index+1,end)
    return v
def sortingAlgorithm(v,start,end):
        pivot=random.randrange(start,end)
        v[pivot],v[end]=v[end],v[pivot]
        pivot=end;
        pivotvalue=v[pivot]
        indexforcomparison=start


        for i in range (start,end):
            if v[i]<=pivotvalue:
                v[i],v[indexforcomparison]=v[indexforcomparison],v[i]
                indexforcomparison+=1
        v[indexforcomparison],v[pivot]=v[pivot],v[indexforcomparison]
        return indexforcomparison

#SHELL SORT
def call_ShellSort(v):
    n=len(v)
    return ShellSort(v,n)
def ShellSort(v,n):
    gap=n//2
    #folosim un while pentru a imparti vectorul la 2 pana cand rezultatul este mai mic decat 1
    while gap>=1:
        #urmatorul for va numara elementele incepand cu elementul de la pozitia gap
        for i in range(gap,n):
            j=i-gap
            while j>=0:
                if v[j+gap]>v[j]:
                    break
                else:
                    v[j+gap],v[j]=v[j],v[j+gap]
                j=j-gap
        gap=gap//2
    return v

#RADIX SORT
def call_RadixSort(v):
    n=len(v)
    return RadixSort(v,n)
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
    b= [0]* (n)

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


Sorts=[call_counting_sort, call_interclasare, call_QuickSort,call_ShellSort,call_RadixSort]


f=open("test_calc.txt")
T=f.readline()
for i in range(len(T)):
    if T[i]=="=":
        Nr=int(T[i+1:].strip())
        break
T=f.readline()
while T!='':
    T=T.split()
    N=int(T[0][2:])
    MAX = int(T[1][4:])
    print("N="+str(N))
    print("MAX="+str(MAX))
    array=[]
    array.append(MAX)
    if N<=100000000:
        for i in range(N-1):
            array.append(random.randint(0,MAX))
        for s in Sorts:
            Timp_start=time.time()
            s(array)
            Timp_end=time.time()
            timp=Timp_end-Timp_start
            print(f"Timp Diferenta:{timp}")
    T = f.readline()
import random
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

v=[7, 5, 0, 0, 91, 87, 2, 2]
start=0
end=len(v)-1
print(QuickSort(v,start,end))


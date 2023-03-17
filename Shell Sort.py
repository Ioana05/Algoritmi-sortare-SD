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


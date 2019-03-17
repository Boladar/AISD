def buduj_kopiec(tablica,n,indeks):
    zamiana=indeks
    lewy=indeks*2+1
    prawy=indeks*2+2
    if lewy<n and tablica[lewy]>tablica[zamiana]:
        zamiana=lewy
    if prawy<n and tablica[prawy]>tablica[zamiana]:
        zamiana=prawy
    if indeks!=zamiana:
        t = tablica[indeks]
        tablica[indeks] = tablica[zamiana]
        tablica[zamiana] = t
        buduj_kopiec(tablica,n,zamiana)

def heapSort(tablica):
    n=len(tablica)
    if len(tablica)%2==0:
        j=int(len(tablica)/2-1)
    else:
        j=int(len(tablica)/2)
    for i in range(j,-1,-1):
        buduj_kopiec(tablica,n,i)
    for i in range(n-1,0,-1):
        tymczasowa=tablica[0]
        tablica[0]=tablica[i]
        tablica[i]=tymczasowa
        n-=1
        buduj_kopiec(tablica,n,0)
    return tablica

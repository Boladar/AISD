def przerwa(tablica):
    h=0
    while h<len(tablica):
        h=3*h+1
    return h

def shellSort(tablica):
    h=przerwa(tablica)
    while (h):
        for i in range(h,len(tablica),h):
            tymczasowa=tablica[i]
            j=i-h
            while j>=0 and tablica[j]>tymczasowa:
                tablica[j+h]=tablica[j]
                j-=h
            tablica[j+h]=tymczasowa
        h=int((h-1)/3)
    return tablica
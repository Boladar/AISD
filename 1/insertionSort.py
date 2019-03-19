def insertionSort(tablica):
    tymczasowa = 0
    for i in range(1,len(tablica)):
        tymczasowa = tablica[i]
        j=i-1
        while j>=0 and tablica[j]>tymczasowa:
            tablica[j+1]=tablica[j]
            j-=1
        tablica[j+1]=tymczasowa
    return tablica


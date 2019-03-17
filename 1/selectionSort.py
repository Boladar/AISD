def selectionSort(tablica):
    for i in range(len(tablica)-1):
        for j in range(i,len(tablica)):
            if tablica[i]>tablica[j]:
                tymczasowa = tablica[i]
                tablica[i] = tablica[j]
                tablica[j] = tymczasowa
    return tablica

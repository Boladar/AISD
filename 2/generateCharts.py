from generateNumbers import generateNumbers
from linked_list import *
import time
import random

'''
tab = generateNumbers(10)
ll = Linked_list()
for n in tab:
    ll.add_element(n)

ll.print_list()

ll.delete_list()

ll.print_list()
'''

TEST_SIZES = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
#TEST_SIZES = [10000,20000]
TEST_FUNC = ["Wyszukiwanie N/10 elementów", "Usuwanie Całej struktury <iter>","Usuwanie Całej struktury <garbage collector>"]

creation_times = []
find_times = []
destruction_times = []
func_traces = []

for s in TEST_SIZES:
    print("creation test for size of: {}".format(s))
    #creation
    tab = generateNumbers(s)

    start = time.time()
    ll = Linked_list()
    for x in range(s):
        ll.add_element(x)

    end = time.time()
    creation_times.append(end-start)


    print("searching test for size of: {}".format(s))
    #searching
    picked_numbers = []
    for i in range(int(s/10)):
        picked_numbers.append(random.choice(tab))
    
    start = time.time()

    for n in picked_numbers:
        ll.find_element(n)

    end = time.time()

    find_times.append(end-start)
    
    print("deletion test for size of: {}".format(s))
    #deletion
    start = time.time()

    ll.delete_list()

    end = time.time()

    destruction_times.append(end-start)


#write to files
f = open("creation_times.txt","w")
for r in creation_times:
    f.write(str(r) + "\n")
f.close()

f = open("search_times.txt","w")
for r in find_times:
    f.write(str(r) + "\n")
f.close()

f = open("destructoin_times.txt","w")
for r in destruction_times:
    f.write(str(r) + "\n")
f.close()
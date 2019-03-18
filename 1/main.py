import plotly.plotly
import plotly.graph_objs as go

import time
import generate

#import test func
from heapSort import heapSort
from insertionSort import insertionSort
from selectionSort import selectionSort
from shellSort import shellSort

#import data types
from generate import *

TEST_SIZES = [1000,5000,10000,15000,20000]
FUNC = [heapSort,insertionSort]
DATA_TYPES = [up,down,a,v,stale,randomised]

for f in FUNC:
    func_traces = []
    for d in DATA_TYPES:
        times = []
        for s in TEST_SIZES:
            data = d(s)
            print("sort: {}, data: {} size: {}".format(f.__name__,d.__name__,s))
            start = time.time()
            f(data.copy())
            end = time.time()
            times.append(end-start)

        func_traces.append(go.Scatter(x = TEST_SIZES,y = times,mode = 'lines', name=d.__name__))

    plotly.offline.plot(func_traces,filename="charts/{}.html".format(f.__name__))
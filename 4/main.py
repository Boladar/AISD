import generate
from copy import deepcopy
from euler import euler
from hamilton import hamilton
import plotly.plotly
import plotly.graph_objs as go
import time

TEST_SIZES = [10,15,20,25,30,35,40,45,50,55]
SATURATIONS = [0.3,0.7]
euler_traces = []
hamiltonA_traces = []
hamiltonB_traces = []
hamilton_times = []
euler_times = []

def test_func(func,data,size):
    print("func: {}, size: {}".format(func.__name__,size))
    start = time.time()
    func(deepcopy(data))
    end = time.time()

    return end-start

for s in SATURATIONS:
    for ts in TEST_SIZES:
        next_dictionary = None
        while next_dictionary is None:
            next_dictionary = generate.generate_graph(ts,s)
        
        euler_times.append(test_func(euler,next_dictionary,ts))
        hamilton_times.append(test_func(hamilton,next_dictionary,ts))

    euler_traces.append(go.Scatter(x = TEST_SIZES,y = euler_times,mode = 'lines', name="Euler {}%".format(s*100)))
    hamiltonA_traces.append(go.Scatter(x = TEST_SIZES,y = hamilton_times,mode = 'lines', name="Hamilton_A {}%".format(s*100)))

    euler_times.clear()
    hamilton_times.clear()

hamilton_b_times = []
for ts in TEST_SIZES:
    next_dictionary = None
    while next_dictionary is None:
        next_dictionary = generate.generate_graph(ts,0.5)

    while len(next_dictionary[ts-1]) > 1:
        value_to_remove = next_dictionary[ts-1].pop()
        next_dictionary[value_to_remove].remove(ts-1)


    hamilton_b_times.append(test_func(hamilton,next_dictionary,ts))

hamiltonB_traces.append(go.Scatter(x = TEST_SIZES,y = hamilton_b_times,mode = 'lines', name="Hamilton_B 50%"))

plotly.offline.plot(euler_traces,filename="charts/{}.html".format("euler"))
plotly.offline.plot(hamiltonA_traces,filename="charts/{}.html".format("hamilton_a"))
plotly.offline.plot(hamiltonB_traces,filename="charts/{}.html".format("hamilton_b"))
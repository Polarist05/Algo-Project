from index import getPrimAlgorithm
from scipy.optimize import curve_fit
import timeit
import matplotlib.pyplot as plt
from BigO import Logn,Linear,NlogN,N2logN,Square,Cube
import numpy as np
import random as rand

#---------Test Case--------------------

def worstTestCase(n):
    inp = [[(k,j,int(j*(j-1)/2+k))for k in range(j)]for j in range (1,n-1)]
    inp.append([(0,n-1,-1)])
    return np.concatenate(inp) 

def bestTestCase(n):
    return [(j-1,j,5) for j in range(1,n)]

def RandomTest(n):
    node = [0]
    edges = []
    for i in range(1,n):
        r = rand.randint(0,len(node))+1
        rand.shuffle(node)
        for j in node[:r]:
            edges.append((j,i,rand.randint(0,n**2)))
        node.append(i)
    return edges

def benchmark(nodeCount,input,iterations=1):
    return timeit.timeit(lambda: getPrimAlgorithm(nodeCount,input), number=iterations)*1000

def PerformanceTest(maxValue,testCase,sampleAmount):
    nodeCounts = np.linspace(2, maxValue, 50)
    funcs = [Logn,Linear,NlogN,Square,N2logN,Cube]
    execution_times = []
    for n in nodeCounts:
        n = int(n)
        inp = testCase(n)
        execution_times.append(benchmark(n,inp,sampleAmount)) 

    # Fit curves to the data using curve_fit
    predictTime = [func(nodeCounts,*curve_fit(func,nodeCounts,execution_times)[0])  for func in funcs]

    # Calculate RMSE values
    rmses = [np.sqrt(np.mean(np.power((execution_times - predicted) , 2))) for predicted in predictTime]

    # Plot the data and fitted curves
    plt.scatter(nodeCounts, execution_times, label='Actual Data')
    for i in range(len(funcs)):
        plt.plot(nodeCounts, predictTime[i],label=f'({str(funcs[i].__qualname__)} RMSE={rmses[i]:.2f})')
    plt.xlabel('Node Count')
    plt.ylabel('Runtime')
    plt.title('Fitted Curves for Benchmark Data')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    PerformanceTest(202,RandomTest,15)
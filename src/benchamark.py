import matplotlib.pyplot as plt
import sys
import time
from Matrix import Matrix

sys.setrecursionlimit(10000)
SIZE = 2100
j = 2
a = Matrix([[1, 1], [1, 1]])

indexTab = []
simpleTab = []
strassenTab = []

while j <= SIZE:
    time_before = time.time() * 1000.0
    a = a * a
    time_after = time.time() * 1000.0
    simpleTab.append(time_after - time_before)

    time_before = time.time() * 1000.0
    strassen = a.strassen(a)
    time_after = time.time() * 1000.0
    strassenTab.append(time_after - time_before)

    indexTab.append(j)
    j *= 2

    a = a.horizontaljoin(a)
    a = a.verticaljoin(a)

    plt.plot(indexTab, simpleTab, label='Simple')
    plt.plot(indexTab, strassenTab, label='Strassen')
    plt.legend()
    plt.show()
    plt.savefig("out/" + str(j) + ".png")

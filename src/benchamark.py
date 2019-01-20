import calendar
import datetime
import os
import sys
import time
from Matrix import Matrix

# create subdirectory out
if not os.path.exists('../out'):
    os.makedirs('../out')
file = open("../out/out" + str(calendar.timegm(time.gmtime())) + ".csv", "w")

sys.setrecursionlimit(10000)
SIZE = 1000
j = 2
a = Matrix([[1, 1], [1, 1]])

file.write("n;classic;strassen\n")

while j <= SIZE:
    string = ''

    string += str(j) + ";"
    # classic
    time_before = time.time() * 1000.0
    classic = a * a
    time_after = time.time() * 1000.0
    string += str(time_after - time_before) + ';'

    # strassen
    time_before = time.time() * 1000.0
    strassen = a.strassen(a)
    time_after = time.time() * 1000.0
    string += str(time_after - time_before) + '\n'

    file.write(string)
    print(str(j))
    j *= 2

    # prepare matrix
    a = a.horizontaljoin(a)
    a = a.verticaljoin(a)
file.close()

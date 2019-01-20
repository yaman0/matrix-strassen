from Matrix import Matrix
import ast


def inputMatrix():
    print "Get matrix (ex: [[2,3,1],[1,5,6],[4,5,7]]:"
    string = raw_input()
    tab = ast.literal_eval(string)
    return Matrix(tab)


def getTypeMulti():
    print "Strassen(s)/Classic(c):"
    string = raw_input()
    if not len(string) == 1:
        raise ValueError('Need to write 1 char')
    if string == 'c':
        return 1
    if string == 's':
        return 2
    raise ValueError('Need to write c or s')


a = inputMatrix()
b = inputMatrix()
operation = getTypeMulti()
if operation == 1:
    print a.strassen(b)
if operation == 2:
    print a * b

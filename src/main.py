from Matrix import Matrix
#
# d = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
d = [[2,3,4,5],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
d2 = [[4,5,2,2],[2,3,3,4],[2,3,3,4],[2,3,3,4]]
# # d2 = [[4,5,1],[2,3,1]]
a = Matrix(d)
b = Matrix(d2)
print(a.strassen(b))
# a = Matrix([[1,1], [1,1]])
# a=a.horizontaljoin(a)
# print a
# print "rrr"
# a=a.verticaljoin(a)
# print a
# print "rrr"
#
# a=a.horizontaljoin(a)
# print a
# print 'rrrr'
# print(a.verticaljoin(a))

import math


class Matrix:

    @staticmethod
    def split4twomatrix(a, b):
        """
        split 2 matrix in 4 sub matrix
        :param Matrix a: first matrix
        :param Matrix b: second matrix
        :return: result of 8 matrix
        """
        if not a.isSquare() and not b.isSquare():
            raise ValueError('is not squares matrix')
        if not a.lengthi == b.lengthi:
            raise ValueError('A and B hasn\'t same size')

        newSize = a.lengthi / 2

        # prepare matrix
        a11 = []
        a12 = []
        a21 = []
        a22 = []
        b11 = []
        b12 = []
        b21 = []
        b22 = []

        # dividing the matrices in 4 sub-matrices:
        for i in xrange(0, newSize):
            a11.append([])
            a12.append([])
            a21.append([])
            a22.append([])
            b11.append([])
            b12.append([])
            b21.append([])
            b22.append([])
            for j in xrange(0, newSize):
                a11[i].append(a[i][j])
                a12[i].append(a[i][j + newSize])
                a21[i].append(a[i + newSize][j])
                a22[i].append(a[i + newSize][j + newSize])
                b11[i].append(b[i][j])
                b12[i].append(b[i][j + newSize])
                b21[i].append(b[i + newSize][j])
                b22[i].append(b[i + newSize][j + newSize])
        return Matrix(a11), Matrix(a12), Matrix(a21), Matrix(a22), Matrix(b11), Matrix(b12), Matrix(b21), Matrix(b22)

    def __init__(self, data):
        """
        Constructor
        :param list[] data: list represent a matrix
        """
        self.data = data
        self.lengthi = len(data)
        if self.lengthi != 0:
            if not type(self.data[0]) is list:
                raise ValueError('Matrix need to have 2 dimensions')
            self.lengthj = len(data[0])
        else:
            self.lengthj = 0

    def __add__(self, matrix):
        """
        Add with an orther Matrix
        :param Matrix matrix: other matrix
        :return Matrix:
        """
        result = self.data
        if self.lengthi == matrix.lengthi and self.lengthj == matrix.lengthj:
            for i in range(self.lengthi):
                for j in range(self.lengthj):
                    result[i][j] = self[i][j] + matrix[i][j]
        else:
            raise ValueError('a and b length isn\'t equal')
        return Matrix(result)

    def __getitem__(self, index):
        """
        get data's row from index
        :param int index: index
        :return list: row
        """
        return self.data[index]

    def __str__(self):
        """
        return string representation of Matrix
        :return: string representation
        """
        string = ""
        for i in range(self.lengthi):
            string += str(self.data[i])
            if i != self.lengthi - 1:
                string += "\n"
        return string

    def __mul__(self, other):
        """
        classical multiplication of matrix
        :param Matrix other: other Matrix
        :return Matrix: result
        """
        if self.lengthj != other.lengthi:
            raise ArithmeticError("a.lengthj != b.lengthi")
        result = []
        for i in range(0, self.lengthi):
            line = []
            for j in range(0, other.lengthj):
                value = 0
                for x in range(0, other.lengthi):
                    value += self[i][x] * other[x][j]
                line.append(value)
            result.append(line)
        return Matrix(result)

    def strassen(self, other):
        """
        strassen multiplication of matrix
        :param Matrix other: other Matrix
        :return Matrix: result
        """
        selfaddnumber = 0
        otheraddnumber = 0
        if not self.isSquare() or not other.isSquare():
            raise ValueError("Matrix need to be square")
        if self.lengthi != other.lengthi:
            raise ValueError("Can't multiplication of matrix (not equals size)")
        if self.lengthi % 2 != 0:
            newself, selfaddnumber = self.fillMatrixToSquare()
            other, otheraddnumber = other.fillMatrixToSquare()
            self.data = newself.data.copy()

        if self.lengthi == 2:
            q1 = (self[0][0] - self[0][1]) * other[1][1]
            q2 = (self[1][0] - self[1][1]) * other[0][0]
            q3 = self[1][1] * (other[0][0] + other[1][0])
            q4 = self[0][0] * (other[0][1] + other[1][1])
            q5 = (self[0][0] + self[1][1]) * (other[1][1] - other[0][0])
            q6 = (self[0][0] + self[1][0]) * (other[0][0] + other[0][1])
            q7 = (self[0][1] + self[1][1]) * (other[1][0] + other[1][1])

            c11 = q1 - q3 - q5 + q7
            c12 = q4 - q1
            c21 = q2 + q3
            c22 = - q2 - q4 + q5 + q6
            return Matrix([[c11, c12], [c21, c22]])
        else:
            a11, a12, a21, a22, b11, b12, b21, b22 = Matrix.split4twomatrix(self, other)
            c11 = a11.strassen(b11) + a12.strassen(b21)
            c12 = a11.strassen(b12) + a12.strassen(b22)
            c21 = a21.strassen(b11) + a22.strassen(b21)
            c22 = a21.strassen(b12) + a22.strassen(b22)
            top = c11.horizontaljoin(c12)
            bot = c21.horizontaljoin(c22)
            result = top.verticaljoin(bot)
            return result.removeMatrixBorder(selfaddnumber) if selfaddnumber != 0 else result

    def horizontaljoin(self, other):
        """
        join horizontally 2 Matrix
        :param Matrix other: other matrix
        :return Matrix: result
        """
        result = []
        if self.lengthi == other.lengthi:
            for k in range(0, self.lengthi):
                line = self[k][:]
                line.extend(other[k])
                result.append(line)
            return Matrix(result)
        else:
            raise ValueError("Need a.lengthi == b.lengthi")

    def verticaljoin(self, other):
        """
        join verticaly 2 Matrix
        :param Matrix other: other matrix
        :return Matrix: result
        """
        if self.lengthj == other.lengthj:
            result = self.data
            result.extend(other.data)
            return Matrix(result)
        else:
            raise ValueError("Need a.lengthj == b.lengthj")

    def isSquare(self):
        """
        test if it's an N*N matrix
        :return boolean: test
        """
        return self.lengthi == self.lengthj

    def fillMatrixToSquare(self):
        """
        Fill matrix with 0 to have a 2^nx2^n
        :return:
        """
        target = int(math.ceil(self.lengthi / 2.0))
        diff = int(2 ** target - self.lengthi)
        if not diff == 0:
            right = [[0 for j in range(0, diff)] for i in range(0, self.lengthi)]
            bot = [[0 for j in range(0, 2 ** target)] for i in range(0, diff)]
            new = self.horizontaljoin(Matrix(right))
            new = new.verticaljoin(Matrix(bot))
            return new, diff
        else:
            return self, 0

    def removeMatrixBorder(self, x):
        """
        Remove x border of the matrix
        :param int x:
        :return Matrix:
        """
        return Matrix([[self[i][j] for j in range(0, self.lengthj - x)] for i in range(0, self.lengthi - x)])

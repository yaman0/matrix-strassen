class Matrix:
    def __init__(self, data):
        self.data = data
        self.lengthi = len(data)
        if self.lengthi != 0 :
            if not type(self.data[0]) is list:
                raise ValueError('Matrix need to have 2 dimensions')
            self.lengthj = len(data[0])
        else:
            self.lengthj = 0

    def __add__(self, matrix):
        result = self.data
        if self.lengthi == matrix.lengthi:
            if self.lengthj == matrix.lengthj:
                for i in range(self.lengthi):
                    for j in range(self.lengthj):
                        result[i][j] = self[i][j] + matrix[i][j]
        return Matrix(result)

    def __getitem__(self, item):
        return self.data[item]

    def __str__(self):
        string = ""
        for i in range(self.lengthi):
            string += str(self.data[i])
            if i != self.lengthi - 1:
                string += "\n"
        return string

    def __mul__(self, other):
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

    def submatrix(self, x, y):
        result = []
        for i in range(x[0], y[0]+1): #TODO remove loop
            if x[1] == y[1]:
                result.append([self.data[i][x[1]]])
            else:
                result.append(self.data[i][x[1]:y[1]+1])
        return Matrix(result)

    def strassen(self, other):
        #TODO fill with 0 when 3x3 ...
        if self.lengthi!=other.lengthi and self.lengthj!=other.lengthj:
            raise ValueError("Size not equals and n%2=0")
        if self.lengthi==2 and self.lengthj==2 and other.lengthi==2 and other.lengthj==2:
            q1 = (self[0][0]-self[0][1])*other[1][1]
            q2 = (self[1][0]-self[1][1])*other[0][0]
            q3 = self[1][1]*(other[0][0]+other[1][0])
            q4 = self[0][0]*(other[0][1]+other[1][1])
            q5 = (self[0][0]+self[1][1])*(other[1][1]-other[0][0])
            q6 = (self[0][0]+self[1][0])*(other[0][0]+other[0][1])
            q7 = (self[0][1]+self[1][1])*(other[1][0]+other[1][1])

            c11 = q1 - q3 - q5 + q7
            c12 = q4 - q1
            c21 = q2 + q3
            c22 = - q2 - q4 + q5 + q6
            return Matrix([[c11,c12],[c21,c22]])
        else:
            a11, a12, a21, a22 = self.split4()
            b11, b12, b21, b22 = other.split4()
            c11 = a11.strassen(b11)+a12.strassen(b21)
            c12 = a11.strassen(b12)+a12.strassen(b22)
            c21 = a21.strassen(b11)+a22.strassen(b21)
            c22 = a21.strassen(b12)+a22.strassen(b22)
            top = c11.horizontaljoin(c12)
            bot = c21.horizontaljoin(c22)
            return top.verticaljoin(bot)

    def horizontaljoin(self, other):
        result = []
        if self.lengthi == other.lengthi:
            for k in range(0,self.lengthi):
                line = self[k][:]
                line.extend(other[k])
                result.append(line)
            return Matrix(result)
        else:
            raise ValueError("Need a.lengthi == b.lengthi")

    def verticaljoin(self, other):
        if self.lengthj == other.lengthj:
            result = self.data
            result.extend(other.data)
            return Matrix(result)
        else:
            raise ValueError("Need a.lengthj == b.lengthj")

    def split4(self):
        a11 = self.submatrix([0,0],[(self.lengthi/2)-1,(self.lengthj/2)-1])
        a12 = self.submatrix([0,(self.lengthj/2)],[(self.lengthi/2)-1,self.lengthj-1])
        a21 = self.submatrix([(self.lengthi/2),0],[self.lengthi-1,(self.lengthj/2)-1])
        a22 = self.submatrix([(self.lengthi/2),(self.lengthj/2)],[self.lengthi-1,self.lengthj-1])
        return a11, a12, a21, a22

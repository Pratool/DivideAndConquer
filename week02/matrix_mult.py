import numpy as np
import random

class Matrix:
    def __init__(self, matrix=[[]]):
        self.matrix = matrix

    def __getitem__(self, i):
        return self.matrix[i]

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix)\
                or len(self.matrix[0]) != len(other.matrix[0]):
            print 'Uh oh, your matrices do not have the same dimensions.'
            print self
            print
            print other
            return False
        return self.strassen_mult(other)

    def __rmul__(self, other):
        return other.__mul__(self)

    def __str__(self):
        out = ""
        max_len = 0
        for row in self.matrix:
            for i in row:
                if len(str(i)) > max_len:
                    max_len = len(str(i))
        max_len += 1
        for row in self.matrix:
            out += '[ '
            for el in row:
                str_el = str(el)
                out += str_el + ' '*(max_len - len(str_el))
            out += ']\n'
        return out[:len(out)-1]

    def __len__(self):
        return len(self.matrix)

    def strassen_mult(self, other):
        """
        Assume A and B are both square matrices of the same dimensions.
        """
        A = self.matrix
        B = other.matrix

        if len(A) < 3:
            return self.simple_mult(other)

        out_matrix = Matrix([ [0 for i in range(len(A))] for j in range(len(A)) ])

        mid = int(len(A)/2.0 + 0.5)
        a = Matrix([ row[:mid] for row in A[:mid] ])
        b = Matrix([ row[mid:] for row in A[:mid] ])
        c = Matrix([ row[:mid] for row in A[mid:] ])
        d = Matrix([ row[mid:] for row in A[mid:] ])

        e = Matrix([ row[:mid] for row in B[:mid] ])
        f = Matrix([ row[mid:] for row in B[:mid] ])
        g = Matrix([ row[:mid] for row in B[mid:] ])
        h = Matrix([ row[mid:] for row in B[mid:] ])

        p1 = a*(f-h)
        p2 = (a+b)*h
        p3 = (c+d)*e
        p4 = d*(g-e)
        p5 = (a+d)*(e+h)
        p6 = (b-d)*(g+h)
        p7 = (a-c)*(e+f)

        top_left = p5 + p4 - p2 + p6
        top_right = p1 + p2
        bottom_left = p3 + p4
        bottom_right = p1 + p5 - p3 - p7

        for i in range(len(out_matrix[:mid])):
            for j in range(len(out_matrix[:mid])):
                out_matrix[i][j] = top_left[i][j]

        for i in range(len(out_matrix[:mid])):
            for j in range(mid, len(out_matrix)):
                out_matrix[i][j] = top_right[i][j-mid]

        for i in range(mid, len(out_matrix)):
            for j in range(len(out_matrix[:mid])):
                out_matrix[i][j] = bottom_left[i-mid][j]

        for i in range(mid, len(out_matrix)):
            for j in range(mid, len(out_matrix)):
                out_matrix[i][j] = bottom_right[i-mid][j-mid]

        return out_matrix

    def simple_mult(self, other):
        """
        Assume A and B are both square matrices of the same dimensions.
        """
        A = self.matrix
        B = other.matrix

        if len(A) == 1:
            return Matrix([[A[0][0] * B[0][0]]])

        if len(A) == 2:
            a = A[0][0]
            b = A[0][1]
            c = A[1][0]
            d = A[1][1]
            e = B[0][0]
            f = B[0][1]
            g = B[1][0]
            h = B[1][1]
            return Matrix([[a*e+b*g, a*f+b*h], [c*e+d*g, c*f+d*h]])

        out_matrix = Matrix([ [0 for i in range(len(A))] for j in range(len(A)) ])

        mid = int(len(A)/2.0 + 0.5)
        a = Matrix([ row[:mid] for row in A[:mid] ])
        b = Matrix([ row[mid:] for row in A[:mid] ])
        c = Matrix([ row[:mid] for row in A[mid:] ])
        d = Matrix([ row[mid:] for row in A[mid:] ])

        e = Matrix([ row[:mid] for row in B[:mid] ])
        f = Matrix([ row[mid:] for row in B[:mid] ])
        g = Matrix([ row[:mid] for row in B[mid:] ])
        h = Matrix([ row[mid:] for row in B[mid:] ])

        top_left = (a*e) + (b*g)
        top_right = (a*f) + (b*h)
        bottom_left = (c*e) + (d*g)
        bottom_right = (c*f) + (d*h)

        for i in range(len(out_matrix[:mid])):
            for j in range(len(out_matrix[:mid])):
                out_matrix[i][j] = top_left[i][j]

        for i in range(len(out_matrix[:mid])):
            for j in range(mid, len(out_matrix)):
                out_matrix[i][j] = top_right[i][j-mid]

        for i in range(mid, len(out_matrix)):
            for j in range(len(out_matrix[:mid])):
                out_matrix[i][j] = bottom_left[i-mid][j]

        for i in range(mid, len(out_matrix)):
            for j in range(mid, len(out_matrix)):
                out_matrix[i][j] = bottom_right[i-mid][j-mid]

        return out_matrix

    def __add__(self, other):
        added_matrix = []
        for row_a, row_b in zip(self.matrix, other.matrix):
            cur_row = []
            for a, b in zip(row_a, row_b):
                cur_row.append(a + b)
            added_matrix.append(cur_row)
        return Matrix(added_matrix)
    
    __radd__ = __add__

    def __neg__(self):
        negated_matrix = []
        for row in self.matrix:
            negated_matrix.append([])
            for el in row:
                negated_matrix[-1].append(-1*el)
        return Matrix(negated_matrix)

    def __sub__(self, other):
        return self + (-other)

    def latex(self):
        out = "\\documentclass{article}\n"
        out += "\\usepackage{amsmath}\n"
        out += "\\begin{document}\n"
        out += "\n"
        out += "\\[\n"
        out += "M=\n"
        out += "  \\begin{bmatrix}\n"
        for row in self.matrix:
            out += "    "
            for el in row:
                out += " " + str(el) + " &" 
            out = out[:len(out)-2]
            out += "\\\\\n"
        out += "  \\end{bmatrix}\n"
        out += "\\]\n"
        out += "\n"
        out += "\\end{document}\n"
        return out

def test_add_mat():
    A = [range(4) for i in range(4)]
    B = [range(6, 2, -1) for i in range(4)]
    print A
    print B
    print add_mat(A, A)
    print add_mat(B, B)
    print add_mat(A, B)

def test_latex_mat():
    C = Matrix([[int(random.random()*1000.0) for i in range(32)] for j in range(32)])
    D = Matrix([[int(random.random()*1000.0) for i in range(32)] for j in range(32)])
    print C.latex()

def test_sub_mat():
    A = Matrix([range(4) for i in range(4)])
    B = Matrix([range(6, 2, -1) for i in range(4)])
    print A
    print
    print B
    print
    print A-B

def check_matrix(A, B):
    for row_a, row_b in zip(A, B):
        for a, b in zip(row_a, row_b):
            if a != b:
                return False
    return True

def compare_numpy_strassen(inputA, inputB):
    A = Matrix(inputA)
    B = Matrix(inputB)
    C = A*B
    numpy_c = np.dot(np.asarray(A), np.asarray(B))
    check = check_matrix(C.matrix, numpy_c)
    print 'Matrix A'
    print Matrix(A)
    print
    print 'Matrix B'
    print Matrix(B)
    print
    print 'A * B'
    print 'Strassen Multiplication'
    print Matrix(C)
    print
    print 'Numpy Calculation'
    print numpy_c
    print
    print 'Strassen = Numpy?', check
    return check

def test_mult():
    A = [range(4) for i in range(4)]
    B = [range(6, 2, -1) for i in range(4)]
    C = [[int(random.random()*1000.0) for i in range(32)] for j in range(32)]
    D = [[int(random.random()*1000.0) for i in range(32)] for j in range(32)]
    E = [[1, 2], [4, 5]]
    all_tests = True

    all_tests &= compare_numpy_strassen(A, A)
    all_tests &= compare_numpy_strassen(A, B)
    all_tests &= compare_numpy_strassen(B, B)
    all_tests &= compare_numpy_strassen(C, C)
    all_tests &= compare_numpy_strassen(C, D)
    all_tests &= compare_numpy_strassen(D, D)
    all_tests &= compare_numpy_strassen(E, E)

    if all_tests:
        print "All tests pass!"
    else:
        print "At least one test failed."

    return all_tests


def main():
    test_mult()

if __name__ == "__main__":
    main()

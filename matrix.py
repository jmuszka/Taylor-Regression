import numpy as np
import pandas as pd


class Matrix:

    A = []
    B = []
    X = []

    def __init__(self, A_list=[1], B_list=[1]):

        rows = len(B_list)
        cols = len(A_list)//rows

        for entry in A_list: 
            if type(entry)!=float and type(entry)!=int: raise ValueError("Matrix must consist of Real numbers")
        for entry in B_list: 
            if type(entry)!=float and type(entry)!=int: raise ValueError("Vector must consist of Real numbers")

        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(A_list[cols*i + j])
            self.A.append(row)

        self.A = np.array(self.A)
        self.B = np.array(B_list)

    def solve(self):
        solution = []
        for entry in np.linalg.lstsq(self.A, self.B, rcond=None)[0]: solution.append(round(entry, 5))
        return solution

    def print(self):

        A = []
        B =[]
        for a in self.A: A.append(a)
        for b in self.B: B.append(b)

        for i in range(len(A)):
            row = A[i]
            print(row, end=" ")
            print(B[i])
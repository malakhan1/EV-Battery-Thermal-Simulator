import numpy as np
import helperfunctions as hf

def pivoting(coeffes, results, scaled, k):
    n = len(coeffes)
    row = k
    tempmax = np.abs(coeffes[k][k] / scaled[k])
    for l in range(k + 1, n):
        temp = np.abs(coeffes[l][k] / scaled[l])
        if temp > tempmax:
            tempmax = temp
            row = l
    if row != k:
        for t in range(k, n):
            coeffes[row][t],  coeffes[k][t] = hf.swap(coeffes[row][t],  coeffes[k][t])
        results[row], results[k] = hf.swap(results[row], results[k])
        scaled[row], scaled[k] = hf.swap(scaled[row], scaled[k])


def bakcsubs(coeffes, RHS):
    n = len(coeffes)
    finaltemparray = [0] * n
    finaltemparray[n - 1] = RHS[n - 1] / coeffes[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += coeffes[i][j] * finaltemparray[j]
        finaltemparray[i] = (RHS[i] - s) / coeffes[i][i]
    return finaltemparray


def gauss(A, b, scaled):
    n = len(b)
    for k in range(0, n - 1, 1):
        pivoting(A, b, scaled, k)
        for i in range(k + 1, n, 1):
            factor = A[i][k] / A[k][k]
            for j in range(k + 1, n, 1):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
    x = bakcsubs(A, b)
    return x
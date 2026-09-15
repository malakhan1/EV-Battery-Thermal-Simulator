import equations_creation as ec
import interpolation as intp
import numpy as np
import matplotlib.pyplot as plt
import thomas as T
import gauss_ithpivoting as g




def swap(a, b):
    return b, a

def choiceofmatrix(gv, fv, ev, rv, coeff_matrix, rhs, scaled):
    while True:
        method = input("What solution method did you choose? (g for gauss/t for thomas): ")
        if method == "g":
            x = g.gauss(coeff_matrix, rhs, scaled)
            break
        elif method == "t":
            x = T.thomas(gv, fv, ev, rv)
            break
        else:
            print("invalid ")
    return x
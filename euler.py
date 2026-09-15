import numpy as np

def RofT(T):
    return 0.012 * (1 - 0.004 * (T - 25))

def IofT(T):
    if T <= 300:
        I = 120
    else:
        I = 120 * np.exp(-0.003 * (T - 300))
    return I

def dTdt(t, Ti, TL, TR, Rx, Req, Tfluid, m, C):
    I = IofT(t)
    R = RofT(Ti)
    Q = I**2 * R
    result = (1 / (m * C)) * (Q - (Ti - TL) / Rx - (Ti - TR) / Rx - (Ti - Tfluid) / Req)
    return result

def euler(numofsteps, Ti, time, dt, TL, TR, Rx, Req, Tfluid, m, C):
    Temp = [0] * numofsteps
    Res = [0] * numofsteps
    Curr = [0] * numofsteps
    Temp[0] = Ti

    for k in range(numofsteps - 1):
        slope = dTdt(time[k], Temp[k], TL, TR, Rx, Req, Tfluid, m, C)
        Temp[k + 1] = Temp[k] + dt * slope
        Res[k] = RofT(Temp[k])
        Curr[k] = IofT(time[k])

    Res[numofsteps - 1] = RofT(Temp[numofsteps - 1])
    Curr[numofsteps - 1] = IofT(time[numofsteps - 1])

    return Temp, Res, Curr

def heun_step(x, y, h, TL, TR, Rx, Req, Tfluid, m, C):
    dy1dx = dTdt(x, y, TL, TR, Rx, Req, Tfluid, m, C)
    ye = y + dy1dx * h
    dy2dx = dTdt(x + h, ye, TL, TR, Rx, Req, Tfluid, m, C)
    slope = (dy1dx + dy2dx) / 2.0
    ynew = y + slope * h
    return x + h, ynew

def heun(numofsteps, Ti, time, dt, TL, TR, Rx, Req, Tfluid, m, C):
    Temp_heun = [0] * numofsteps
    Temp_heun[0] = Ti
    for k in range(numofsteps - 1):
        _, Temp_heun[k + 1] = heun_step(time[k], Temp_heun[k], dt, TL, TR, Rx, Req, Tfluid, m, C)
    return Temp_heun

def getmax(x):
    maxx = x[0]
    for i in range(1, len(x)):
        if x[i] > maxx:
            maxx = x[i]
    return maxx

def getcellindx(x):
    maxx = x[0]
    index = 0
    for i in range(1, len(x)):
        if x[i] > maxx:
            maxx = x[i]
            index = i
    return index + 1
## main
import equations_creation as ec
import interpolation as intp
import numpy as np
import matplotlib.pyplot as plt
import helperfunctions as hp
import euler as eu


file_path = "/Users/malakhani/Downloads/cond.txt"
data_arr2 = np.loadtxt(file_path, skiprows=1, encoding="utf-16")
conductivity = intp.user_interpolation(data_arr2)


temps = data_arr2[:, 0]
conductivities = data_arr2[:, 1]
plt.figure()
plt.scatter(temps, conductivities, color='red', marker='D', label='Data')

x_range = np.arange(-20, 101, 20)
fittedpolyy = [intp.interpolation(data_arr2, 3, xi) for xi in x_range]
plt.plot(x_range, fittedpolyy, color='cyan', marker='s', label='2nd order poly')
plt.xlabel('Temperature (°C)')
plt.ylabel('Thermal Conductivity')
plt.title('Interpolated Thermal Conductivity vs Temperature')
plt.legend()
plt.grid(True)
plt.show()

rhs, coeff_matrix, Tfluid = ec.matrixcreate(conductivity)
scaled = ec.maxinmatrix(coeff_matrix)
rv, gv, fv, ev = ec.thomasmatrix(rhs, coeff_matrix)

x = hp.choiceofmatrix(gv, fv, ev, rv, coeff_matrix, rhs, scaled)
print("x =", x)

cell_indices = list(range(1, 16))
plt.figure()
plt.plot(cell_indices, x, 'o-')
plt.xlabel('Cell index')
plt.ylabel('Temperature in Celsius')
plt.title('Steady-state temperature distribution across battery cells')
plt.grid(True)
plt.show()

# ---- Find hottest cell ----
highesttemp = eu.getmax(x)
hottestcell = eu.getcellindx(x)
print("Hottest cell is # ", hottestcell)
print("its maximum temperature is ", highesttemp)

Ti = x[hottestcell - 1]
TL = x[hottestcell - 2]
TR = x[hottestcell]


m = 0.07
C = 920
Rx = 1.72413
Rtim = 0.44642
RA = 0.056818
Rcol = 1 / (436 * conductivity * 0.0016)
Req = Rtim + Rcol + RA

dt = 5
t_end = 900
time = list(range(0, t_end + dt, dt))
numofsteps = len(time)


Temp, Res, Curr = eu.euler(numofsteps, Ti, time, dt, TL, TR, Rx, Req, Tfluid, m, C)
Temp_heun = eu.heun(numofsteps, Ti, time, dt, TL, TR, Rx, Req, Tfluid, m, C)

plt.figure()
plt.plot(time, Temp, '-', label='Euler')
plt.plot(time, Temp_heun, '--', label='Heun')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title(f'Hottest cell temperature during fast charging (Δt = {dt} s)')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(time, Res, '-')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (ohms)')
plt.title('Hottest cell resistance during fast charging')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(time, Curr, '-')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('Charging current profile')
plt.grid(True)
plt.show()


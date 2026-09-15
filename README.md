# EV Battery Thermal Simulator

A 1-D transient thermal simulator for an electric vehicle (EV) battery developed in Python.

## Project Overview

This project simulates the temperature behavior of a 15-cell lithium-ion battery during:

- Steady-state operation
- Fast charging
- Transient thermal conditions

## Numerical Methods

The project uses:

- 2nd-order Newton interpolation
- Linear system solution using Gauss elimination & Thomas method
- Euler method for solving the transient differential equation

## Project Structure

- `main.py` — Main program
- `interpolation.py` — Newton interpolation
- `steady_state.py` — Steady-state thermal analysis
- `transient.py` — Transient analysis
- `helperfunctions.py`- Helping functions used in code


## Course

ENGR 3202 — Engineering Analysis and Computation I  
The American University in Cairo

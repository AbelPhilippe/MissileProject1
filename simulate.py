# Simulate the SprintABM

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

# Import modules
from propulsion import *

# ---------------------------------------------
#      Ṕositional parameters - SPRINT ABM
# ---------------------------------------------

px = 0.0
py = 0.0
pz = 0.0

vx = 0.0
vy = 0.0
vz = 0.0



# =============================================
#            Physical parameters
# =============================================

g = 9.81               # m/s^2, acceleration due to gravity
rho = 1.225            # kg/m^3, air density at sea level
Cd = 0.75              # Drag coefficient (assumed constant)



A = 0.01               # m^2, cross-sectional area of the missile
m = 3.500              # kg, mass of the missile
length = 8.2           # m, length of the missile
diameter = 1.3         # m, diameter of the missile




calculate_mass_change = propulsion.calculate_mass_change
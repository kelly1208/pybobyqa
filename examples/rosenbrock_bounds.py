# Py-BOBYQA example: minimize the Rosenbrock function with bounds
from __future__ import print_function
import numpy as np
import pybobyqa

# Define the objective function
def rosenbrock(x):
    return 100.0 * (x[1] - x[0] ** 2) ** 2 + (1.0 - x[0]) ** 2

# Define the starting point
x0 = np.array([-1.2, 1.0])

# Define bound constraints (lower <= x <= upper)
lower = np.array([-10.0, -10.0])
upper = np.array([0.9, 0.85])

# For optional extra output details
#import logging
#logging.basicConfig(level=logging.INFO, format='%(message)s')

# Call Py-BOBYQA (with bounds)
soln = pybobyqa.solve(rosenbrock, x0, bounds=(lower,upper))

# Display output
print(soln)


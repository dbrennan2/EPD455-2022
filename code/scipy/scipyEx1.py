from scipy.optimize import root
from math import exp

# equation solved is exp(z)+z=0
def eqn(z):
  return exp(z) + z

# initial guess: -1.0
myroot = root(eqn, -1.0)

print(myroot.x)

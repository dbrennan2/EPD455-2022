import numpy as np
import matplotlib.pyplot as plt
from math import exp


x = np. linspace(-1, 0, 100)
y = np.exp(x)

plt.plot(x, -x, 'b-', label='$-x$')
plt.plot(x, y, 'g+', label='$exp(x)$')
plt.legend()
plt.title('Solving $exp(x)+x=0$')
plt.show()
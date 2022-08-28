import numpy as np
import matplotlib.pyplot as plt

A = np.random.random((100, 100))
plt.tight_layout()
plt.imshow(A)
plt.hot()
plt.colorbar()
plt.show()
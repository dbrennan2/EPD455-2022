import numpy as np
import matplotlib.pyplot as plt

data = np.random. randn(1000)
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

# histogram (pdf)
ax1.hist(data, bins=30, color='b', density=True)

# empirical cdf
ax2.hist(data, bins=30, color='r', cumulative=True, density=True)
plt.tight_layout()
plt.show()
plt.savefig('histogram. pdf')
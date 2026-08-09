"""
Description:    This finds local maximums in a 2D matrix
Date:           15-07-2026
"""

import numpy as np
import matplotlib.pyplot as plt

array = np.random.uniform(0, 1, (10, 10))

array[2, 2]

slides = np.array([array[:-2, :-2],
          array[1:-1, :-2],
          array[2:, :-2],
          array[:-2, 1:-1],
          array[2:, 1:-1],
          array[:-2, 2:],
          array[1:-1, 2:],
          array[2:, 2:]
        ])

conditions = np.array([array[1:-1, 1:-1] > slide for slide in slides])

mask = np.all(conditions, axis=0)

y, x = np.where(mask)
y += 1
x += 1

plt.imshow(array, cmap='viridis', interpolation='nearest')
plt.colorbar()

plt.scatter(x, y, s=50, color="red", label="Local Maximum")

plt.legend()
plt.show()


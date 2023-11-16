import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
n_points = 50  
x = np.random.rand(n_points)  
y = np.random.rand(n_points)  
plt.scatter(x, y, label='Random Data', color='red', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Scatter Plot')
plt.legend()
plt.grid(True)
plt.show()

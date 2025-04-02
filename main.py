import numpy as np
import matplotlib.pyplot as plt

# 2D standard normal vectors
np.random.seed(0)
n = 1000
X = np.random.randn(n, 2)  # Each row is a sample from N(0, I)

# 2D rotation matrix (e.g., 45 degrees)
theta = np.pi / 4
Q = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# apply rotation
Y = X @ Q.T 

# plot original and rotated distributions
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].scatter(X[:, 0], X[:, 1], alpha=0.3)
axs[0].set_title("Original N(0, I)")
axs[0].axis("equal")

axs[1].scatter(Y[:, 0], Y[:, 1], alpha=0.3, color='orange')
axs[1].set_title("Rotated N(0, I)")
axs[1].axis("equal")

plt.suptitle("Standard Normal Vectors Before and After Rotation")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import 

theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)
theta0, theta1 = np.meshgrid(theta0_vals, theta1_vals)

# cost function: J(theta) = (theta0 + theta1 * x - y)^2 for x=2, y=5
x = 2
y = 5
J = (theta0 + theta1 * x - y) ** 2

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta0, theta1, J, cmap='viridis', alpha=0.9, edgecolor='none')
ax.set_xlabel(r'$\theta_0$')
ax.set_ylabel(r'$\theta_1$')
ax.set_zlabel(r'$J(\theta)$')
ax.set_title('Convex Cost Function for Linear Regression')
plt.tight_layout()
plt.show()


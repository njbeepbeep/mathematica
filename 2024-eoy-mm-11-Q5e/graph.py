import numpy as np
import matplotlib.pyplot as plt

# Define the inverse function g^(-1)(x)
def g_inverse(x):
    return (3 - 3**(x / 2)) / 2

# Define the function h(x) = g^(-1)(x) + k
def h(x, k):
    return g_inverse(x) + k

# Define the range of x values for plotting
x_values = np.linspace(-2, 3, 500)

# Plot h(x) for different values of k
k_values = [-2, -1, 0, 1, 2]  # Example k values
plt.figure(figsize=(10, 6))

for k in k_values:
    y_values = h(x_values, k)
    plt.plot(x_values, y_values, label=f'h(x) with k = {k}')

# Plot axes
plt.axhline(0, color='black', linewidth=0.8, linestyle='--', label='y = 0')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--', label='x = 0')

# Add labels and legend
plt.title("Graph of h(x) = g^(-1)(x) + k for Various k Values")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

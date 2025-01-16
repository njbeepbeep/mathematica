from sympy import symbols, solve, log, simplify

# Define variables
x, k = symbols('x k')

# Define the inverse function g^(-1)(x)
g_inverse = (3 - 3**(x/2)) / 2

# Define the function h(x) = g^(-1)(x) + k
h = g_inverse + k

# Solve for the x-intercept of h(x), i.e., h(x) = 0
x_intercept = solve(h, x)

# Find the condition for the x-intercept to be negative
condition = solve(x_intercept[0] < 0, k)

# Output the condition on k
print("The condition on k for a negative x-intercept is:")
print(condition)
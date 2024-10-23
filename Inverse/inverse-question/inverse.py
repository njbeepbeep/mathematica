import sympy as sp

t, y = sp.symbols('t, y')

I = 0.2*2**((-t/8))

inverse_solution = sp.solve(y - I, t)
inverse_function = sp.simplify(inverse_solution[0])

print(inverse_solution)
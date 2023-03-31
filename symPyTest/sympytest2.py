import sympy as sp
alpha, beta, gamma = sp.symbols("alpha, beta, gamma")
exp = alpha*x**3+3*x**3
#sp.simplify(exp)
sp.collect(y,x**3)

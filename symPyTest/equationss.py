import sympy as sp
x,y = sp.symbols("x,y")
eq1 = sp.Eq(2*x+y-5)
eq2 = sp.Eq(x-y-1)
sol = sp.solve((eq1,eq2),(x,y))
sol
print(f"The solution of x is {sol[x]} and y is {sol[y]}")

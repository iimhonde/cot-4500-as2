
from src.main.assignment_1 import (
    bisection_method, 
    fixed_point,
    newton_raphson, 
    approx_alg
)


def f(x):
    return x**3 - x - 2  

root = bisection_method(f, 1, 2, 1e-6, 100)
print(f"bisection method root: {root}") 

  
def g(x):
    return (x + 2 / x) / 2 

root = fixed_point(g, 1.5, 1e-6, 100)
print(f"fixed point root: {root}") 

    
def f(x):
    return x**3 - x - 2 

def df(x):
    return 3*x**2 - 1 

root = newton_raphson(f, df, 1.5, 1e-6, 100)
print(f"newton_raphson root: {root}") 


def f(x):
    return (x - 3)**2 

min_x = approx_alg(f, 0, 6, 100)
print(f"Computed min_x: {min_x}") 


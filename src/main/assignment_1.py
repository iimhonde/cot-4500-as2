import numpy as np

def approx_alg(f, a, b, num_points):
    
    x_values = np.linspace(a, b, num_points * 100)  
    min_x = x_values[np.argmin([f(x) for x in x_values])] 
    return min_x

def bisection_method(f, left, right, tol, max_iter):
    i = 0

    while abs(left + right) > tol and i < max_iter:
        i+= 1
        p = (left + right) / 2

        if( (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0) ) :
            right = p
        else: 
            left = p
    return p
        
def fixed_point(g, init_approx, tol, max_iter):
    i = 0
    while(i <= max_iter):
        p = g(init_approx)
        if abs(p - init_approx) < tol:
            return p
        init_approx = p
        i+=1
    return None

def newton_raphson (f, df,  init_approx, tol, max_iter):
    i = 0
    while i < max_iter:
        p = init_approx - f(init_approx) / df(init_approx)
        if(abs(p - init_approx) < tol):
            return p
        
        init_approx = p
        i += 1
    return None



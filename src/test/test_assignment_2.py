
from src.main.assignment_2 import (
    neville, divided, newton_poly, hermite, cubic_spline

)


#Neville's method

x = [3.6, 3.8, 3.9]
f = [1.675, 1.436, 1.318]
w = 3.7

approx = neville(x, f, w)
print(f" {approx:.16f}")





#Divided Difference
xi = [7.2, 7.4, 7.5, 7.6]
fi = [23.5492, 25.3913, 26.8224, 27.4589]
x =7.3
poly = newton_poly(xi, fi, x)
approx = divided(xi, fi)

print(f"\n{approx[1][1]:.16f}") 
print(f"{approx[2][2]:.16f}") 
print(f"{approx[3][3]:.16f}") 

print(f"\n{poly}")
print("\n")

#Hermite Polynomial Approximation
x = [3.6, 3.8, 3.9]
f = [1.675, 1.436, 1.318]
fp = [-1.195, -1.188, -1.182]
hermite_diffs = hermite(x, f, fp)
for row in hermite_diffs:
    formatted_row = ["{:>10.6e}".format(val) for val in row] 
    print("[ " + "  ".join(formatted_row) + " ]")  

#Cubic spline interpolation

x_vals = [2,5,8,10]
f_vals = [3, 5,7,9 ]

A, b, x = cubic_spline(x_vals, f_vals)

for row in A:
    print(row)

print(f" {b}")
print(f" {x}")
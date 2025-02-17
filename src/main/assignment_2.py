import numpy as np

def neville(x, f, w):
    n = len(x)
    nev = [[0.0]  * n for _ in range(n)]
    for i in range(n):
        nev[i][0] = f[i]

    for i in range(1,n):
        for j in range(1, i +1):
            term1 = (w - x[i - j]) * nev[i][j - 1]
            term2 = (w - x[i]) * nev[i - 1][j - 1]
            nev[i][j] = (term1 - term2) / (x[i] - x[i - j])

    
    return nev[2][2]

#def newtonFor()

def divided(xi, fi):
   lim = len(xi)
   diffs = [[0.0] *  lim for _ in range(lim)]

   for i in range(lim):
       diffs[i][0] = fi[i]

   for i in range(1, lim):
       for j in range(1, i + 1):
           diffs[i][j] = (diffs[i][j - 1] - diffs[i - 1][j - 1]) / (xi[i] - xi[i-j])
    
   return diffs

def newton_poly(xi, fi, x):

    diffs = divided(xi, fi)
    
    n = len(xi)
    coeffs = [diffs[i][i] for i in range(n)]
  
    result = coeffs[0]
    product_term = 1.0  

    
    
    for i in range(1, n):
        product_term *= (x - xi[i - 1])
        result += coeffs[i] * product_term
      
    
    return result


def hermite(x, f, fp):
    lim = len(x) * 2
    diffs = [[0.0] * (lim - 1) for _ in range(lim)]

    z_val =[0.0] * lim

   

    for i in range(len(x)):
        diffs[2 * i][0] = x[i] 
        z_val[2 * i] = x[i]

        diffs[2 * i + 1][0] = x[i] 
        z_val[2 * i + 1] = x[i]

        diffs[2 * i][1] = f[i]
        diffs[2 * i + 1][1] = f[i]
        diffs[2*i+1][2] = fp[i]

        if i > 0:
            diffs[2 * i][2] = (diffs[2 * i][1] - diffs[2 * i - 1][1]) / (diffs[2 * i][0] - diffs[2 * i - 1][0])
 

    for i in range(3, lim - 1):  
        for j in range(i - 1, lim):  
            if j - i + 1 >= 0 and z_val[j] != z_val[j - i + 1]:  
                diffs[j][i] = (diffs[j][i - 1] - diffs[j - 1][i - 1]) / (z_val[j] - z_val[j - i + 1])

    return diffs

    



def cubic_spline(x_vals, f_vals):
    n = len(x_vals) - 1 
    A = np.zeros((n + 1, n + 1)) 

    h = np.diff(x_vals)  

   
    A[0, 0] = 1  
    A[n, n] = 1  

    for i in range(1, n): 
        A[i, i - 1] = h[i - 1]  
        A[i, i] = 2 * (h[i - 1] + h[i])  
        A[i, i + 1] = h[i] 

    b = np.zeros(n - 1)
    d = np.diff(f_vals) / h

    b = np.zeros(n + 1)  
    for i in range(1, n):
        b[i] = (6 / h[i]) * (d[i] - d[i - 1])

    x = np.linalg.solve(A,b)
   
    return A, b, x





    

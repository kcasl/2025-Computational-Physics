import math

def root_newton(f, df, guess, tolerance=1.0e-6):
    x = guess
    dx = 2 * tolerance 
    
    while dx > tolerance:
        x1 = x - f(x) / df(x) 
        dx = abs(x - x1) 
        x = x1 
    
    return (f'Found f(x) = 0 at x = {x:.8f} ± {tolerance:.8f}')

def f(x):
    return math.exp(x) ** 2 - 3 * math.exp(x)

def df(x):
    return 2 * x * math.exp(x**2) - 3 * math.exp(x)

print(root_newton(f, df, 1.0))

# output : Found f(x) = 0 at x = -3.14824975 ± 0.00000100
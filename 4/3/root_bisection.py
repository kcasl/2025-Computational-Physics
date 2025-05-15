import math

def root_bisection(f, a, b, tolerance=1.0e-6):
    cnt = 0
    dx = abs(b - a)
    while dx > tolerance:
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        dx = abs(b - a)
        cnt += 1
    return (f'Found f(x) = 0 at x = {x:.8f} ± {tolerance:.8f}', "repeat time:", cnt)

def f(x):
    return math.exp(x) ** 2 - 3 * math.exp(x)

print(root_bisection(f, 1, 10))

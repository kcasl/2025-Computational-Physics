import math

tolerance = 1.0e-6
cnt = 0

def f(x):
    f = x*x - 5
    return f

a, b = map(float, input("Enter two guesses, separated by commas: ").split(','))

dx = abs(b - a)

while dx > tolerance:
    x = (a + b) / 2.0
    
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x
    
    dx = abs(b - a)
    cnt += 1

print(f'Found f(x) = 0 at x = {x:.8f} ± {tolerance:.8f}')
print("repeat time : ", cnt)

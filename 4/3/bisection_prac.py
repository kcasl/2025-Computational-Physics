def f(x):
    return x*x -5

cnt = 0
a = 0
b = 10

tolerance = 0.000001

dx = abs(b - a)

while dx > tolerance:
    x = (a + b) / 2
    
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x
        
    dx = abs(b - a)
    cnt += 1
    
print("f(x) =  x * x - 5")
print(f"Found f(x)=0 at x = {x:.6f} +/- {tolerance:.6f}")
print(f"Bisection step : {cnt}")
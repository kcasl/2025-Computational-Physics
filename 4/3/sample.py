from numpy import *  # numpy functions and constants

# Get the initial guesses
def root_newton(f, df, guess, tolerance=1.0e-6):
    """
    Uses the newton's method to find a value x from a guess a 
    for which f(x) = 0 , to with in the tolerance given.
    Default tolerance is 1.0e-6, if no tolerance is specified in the function call.
    It is required to pass this function both f(x) and df(x).
    """
    dx = 2 * tolerance  # initial dx>delta
    N = 0
    x = guess
    while dx > tolerance:  # Repeat until dx < tolerance
        x1 = x - f(x) / (-1 * df(x))  # temp. (-1) why??
        N += 1
        dx = abs(x - x1)  # update uncertainty in root location
        x = x1
    print("newton step : ", N)
    return x  # answer is x +/- Tolerance

tolerance=1.0e-6
theta_0 = root_newton(cos, -sin, pi/7, tolerance=1.0e-6)
print("Found f (x) = 0 at x = %.8f +/- %0.8f " % (theta_0 , tolerance))
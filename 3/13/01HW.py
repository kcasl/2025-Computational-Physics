# 1
# import pylab as pl

# x = pl.linspace(0, 10, 51)
# y = pl.exp(x)

# pl.plot(x, y, 'b-^')
# pl.xlim(0,10)

# pl.legend(["e^x graph"])
# pl.show()


# 2
# import numpy as np
# import pylab as pl

# def dd(x, epsilon=0.001):
#     return np.where(np.abs(x) < epsilon, 1/epsilon, 0)

# x = pl.linspace(-10, 10, 1001)

# pl.plot(x, dd(x))
# pl.xlabel('x')
# pl.ylabel('y')
# pl.legend(['Dirac Delta Function'])
# pl.grid(True)
# pl.show()


# 3
import numpy as np
import pylab as plt

def sig(x):
    return 1 / (1 + np.exp(-x))

x = np.linspace(-10, 10, 101)

plt.plot(x, sig(x))
plt.xlabel('x')
plt.ylabel('s(x)')
plt.legend(['Sigmoid Function'])
plt.grid(True)
plt.show()
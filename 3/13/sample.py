# import pylab as pl
# x = pl.linspace(0, 10, 51)
# y = 2 * x - 3
# pl.plot(x, y, 'r-')
# pl.show()

import pylab as pl
import math
x = pl.linspace(0, 10, 51)
y = 2 * pow(x,3) + 3 * pow(x,2) - 1
#y = 2 * x ** 3 + 3 * x ** 2 - 1
pl.plot(x, y, 'r-')
pl.show()


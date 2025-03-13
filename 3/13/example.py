import pylab as pl

time = pl.linspace(0, 4*pl.pi, 1001)
height = pl.exp(- time / 3.0) * pl.sin(time * 3)
# pl.figure()

pl.plot(time, height, 'm-^')
pl.plot(time, 0.3 * pl.sin(time * 3), 'g-')
pl.legend(['damped', 'constant amplitude']) #, loc='lower right')
pl.xlabel('Time (s)')
pl.ylabel('height')
pl.show()

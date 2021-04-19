import matplotlib.pyplot as plt
import decimal


# Это замена np.arange
def arange(start, stop, step):
    while start < stop:
        yield start
        start += decimal.Decimal(step)


hyperbola = lambda x: 1 / x


def asymptote_checker(argument, function):
    try:
        function(argument)
        return True
    except ZeroDivisionError:
        return False

xmin = -20
xmax = 20
dx = 0.1

xlist = [round(x, 4) for x in arange(xmin, xmax, dx)]

ylist = [hyperbola(x) if asymptote_checker(x, hyperbola) else float('nan') for x in xlist]

plt.plot(xlist, ylist)
plt.show()
from numpy import random, pi, count_nonzero
import matplotlib.pyplot as plt
import math

def pi_error(n):
    x = 1 - 2 * random.random(int(n))
    y = 1 - 2 * random.random(int(n))

    amount_in_circle = count_nonzero((x*x+y*y)<=1)
    my_pi = 4*amount_in_circle/n

    return abs(pi - my_pi)

xs = [2 ** k for k in range(10, 25)]
ys = [pi_error(x) for x in xs]

plt.plot(xs, ys)
plt.xscale('log')
plt. show()

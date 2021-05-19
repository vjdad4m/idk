import matplotlib.pyplot as plt
from math import sin, cos
import numpy as np

def interpolate(a0, a1, w):
    return (a1 - a0) * w + a0

def random(ix, iy):
    r = 2920 * sin(ix * 21942 + iy * 171324 + 8912) * cos(ix * 23157 * iy * 217832 + 9758)
    return (cos(r), sin(r))

def dot(ix, iy, x, y):
    r = random(ix, iy)
    dx = x - float(ix)
    dy = y - float(iy)
    return (dx*r[0] + dy*r[1])

def perlin(x,y,scale=1):
    x0, y0 = int(x), int(y)
    x1 = x0 + 1
    y1 = y0 + 1
    
    sx = x - x0
    sy = y - y0
    
    n0 = dot(x0, y0, x, y)
    n1 = dot(x1, y0, x, y)
    ix0 = interpolate(n0, n1, sx)
    
    n0 = dot(x0, y1, x, y)
    n1 = dot(x1, y1, x, y)
    ix1 = interpolate(n0, n1, sx)

    val = interpolate(ix0, ix1, sy)
    return val * scale

dT = 0.01
start = 0
end = 100
T = np.arange(start, end, dT)
P = np.array([perlin(x,1) for x in T])

fig, ax = plt.subplots()
ax.plot(T,P)
ax.set_title(f'[ dT: {dT} | start: {start} | end: {end} ]')
ax.set_xlabel('x')
ax.set_ylabel('value')
plt.show()

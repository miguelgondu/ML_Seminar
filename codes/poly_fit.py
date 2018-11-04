import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg
import sympy

def poly_fit(x, t, m):
    A = np.zeros((m+1, m+1))
    for k in range(m+1):
        for i in range(m+1):
            A[k, i] = np.sum(x**(i+k))
    b = np.array([np.sum(t*x**k) for k in range(m+1)])
    w = linalg.solve(A, b)
    return w

x = np.linspace(0, 2*np.pi, 10)
x_bigger = np.linspace(0, 2*np.pi, 100)
t = np.sin(x) + np.random.normal(0, 0.1, 10)
y = np.sin(x_bigger)
plt.plot(x_bigger, y, '--r', label=r'$y=\sin(x)$')
plt.plot(x, t, 'o')

for m in [1, 4, 10]:
    x = np.linspace(0, 2*np.pi, 10)
    w = poly_fit(x, t, m)
    x = sympy.Symbol('x')
    p = sympy.Poly(w[::-1], x) # it's inverted because of the way sympy constructs polys.
    y_fit = np.array([p.subs(x, x_bigger[k]) for k in range(100)])
    plt.plot(x_bigger, y_fit, label='$m={}$'.format(m))

plt.legend()
plt.show()

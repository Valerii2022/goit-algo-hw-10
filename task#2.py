import numpy as np

def monte_carlo_integral(f, a, b, n=10000):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, max(f(x)), n)
    under_curve = y < f(x)
    integral = (b - a) * max(f(x)) * np.sum(under_curve) / n
    return integral

def f(x):
    return x ** 2

a = 0
b = 2

integral_estimate = monte_carlo_integral(f, a, b)
print(f"Оцінка інтегралу методом Монте-Карло: {integral_estimate}")

import scipy.integrate as spi
result, error = spi.quad(f, a, b)
print(f"Інтеграл (функція quad): {result}")

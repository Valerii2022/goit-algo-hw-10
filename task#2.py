import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


def f(x):
    return np.sin(x)

a = 0  
b = np.pi  

x = np.linspace(-0.5, np.pi + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()

ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

N = 10000

x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, 1, N)

points_under_curve = y_random < f(x_random)

integral_mc = (b - a) * np.sum(points_under_curve) / N

print("Інтеграл методом Монте-Карло: ", integral_mc)

result, error = spi.quad(f, a, b)

print("Інтеграл аналітичний: ", result)
print("Абсолютна помилка: ", error)




import numpy as np
import matplotlib.pyplot as plt


p = np.pi
X1 = []
X2 = []
f1 = 0
f2 = p
step = p / 50
while f1 < p+step:
    X1.append(f1)
    f1 += step
while f2 < 2 * p:
    X2.append(f2)
    f2 += step


def f(X):
    y = []
    for x in X:
        y_arg = 0
        for k in range(2, N):
            y_arg += (np.cos(k * x) * ((-1)**k + 1))/((1 - k * k) * p)
        y.append(1 / p + np.sin(x)/2 + y_arg)
    return y

N = int(input("Введите количество слогаемых: "))

fig, ax = plt.subplots()
ax.set_title(f'Общий ряд Фурье {N}-ого порядка')
ax.plot(X1 + X2, f(X1 + X2), label='Ряд Фурье', color='red')
ax.plot(X1, [np.sin(x) for x in X1], label='$f(x)$', color='black', linewidth=1)
ax.plot(X2, [0] * len(X2), color='black', linewidth=1)
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.legend()
plt.show()
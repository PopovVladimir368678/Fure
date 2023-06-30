import numpy as np
import matplotlib.pyplot as plt


p = np.pi
X1 = []
X2 = []
X3 = []
X4 = []
f1 = -2 * p
f2 = -p
f3 = 0
f4 = p
step = p / 50
while f1 < -p and f2 < 0 and f3 < p and f4 < 2 * p:
    X1.append(f1)
    f1 += step
    X2.append(f2)
    f2 += step
    X3.append(f3)
    f3 += step
    X4.append(f4)
    f4 += step


def f(X):
    y = []
    for x in X:
        y_arg = 0
        for k in range(1, 2):
            y_arg += ((-4) + (np.cos((p * (k - 2) / 2)) * (k + 2)) - (
                    np.cos((p * (k + 2) / 2)) * (k - 2)))/(p * (k**2 - 4)) * (np.cos((k * x) / 2))
        for k in range(3, N):
            y_arg += ((-4) + (np.cos((p * (k - 2) / 2)) * (k + 2)) - (
                    np.cos((p * (k + 2) / 2)) * (k - 2)))/(p * (k**2 - 4)) * (np.cos((k * x) / 2))
        y.append(1/p + y_arg)
    return y

N = int(input("Введите количество слогаемых: "))

fig, ax = plt.subplots()
ax.set_title(f'Ряд Фурье по косинусам {N}-ого порядка')
ax.plot(X1 + X2 + X3 + X4, f(X1 + X2 + X3 + X4), label='Ряд Фурье', color='red')
ax.plot(X1, [0] * len(X1), color='black', linewidth=1)
ax.plot(X2, [-np.sin(x) for x in X2], label='$f(x)$', color='black', linewidth=1)
ax.plot(X3, [np.sin(x) for x in X3], color='black', linewidth=1)
ax.plot(X4, [0] * len(X4), color='black', linewidth=1)
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.legend()
plt.show()

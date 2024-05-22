import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметри моделі
a1 = 1.0
a2 = 0.5
b12 = 0.1
b21 = 0.1
c1 = 0.01
c2 = 0.01

# Початкові умови
N1_0 = 10
N2_0 = 5

# Часовий інтервал
t = np.linspace(0, 200, 1000)

# Система диференціальних рівнянь
def competing_species(N, t, a1, a2, b12, b21, c1, c2):
    N1, N2 = N
    dN1_dt = a1 * N1 - b12 * N1 * N2 - c1 * N1**2
    dN2_dt = a2 * N2 - b21 * N1 * N2 - c2 * N2**2
    return [dN1_dt, dN2_dt]

# Розв'язок системи диференціальних рівнянь
N0 = [N1_0, N2_0]
solution = odeint(competing_species, N0, t, args=(a1, a2, b12, b21, c1, c2))
N1 = solution[:, 0]
N2 = solution[:, 1]

# Побудова траєкторій динаміки популяцій
plt.figure(figsize=(12, 5))

# Траєкторії для кожної популяції
plt.subplot(1, 2, 1)
plt.plot(t, N1, label='Вид 1 (N1)')
plt.plot(t, N2, label='Вид 2 (N2)')
plt.xlabel('Час')
plt.ylabel('Чисельність')
plt.title('Траєкторії динаміки популяцій')
plt.legend()
plt.grid()

# Фазовий портрет
plt.subplot(1, 2, 2)
plt.plot(N1, N2)
plt.xlabel('N1')
plt.ylabel('N2')
plt.title('Фазова траєкторія')
plt.grid()

# Знаходження точок спокою
N1_eq1 = 0
N2_eq1 = 0
N1_eq2 = a1 / c1
N2_eq2 = 0
N1_eq3 = 0
N2_eq3 = a2 / c2

plt.plot(N1_eq1, N2_eq1, 'ro', label='Точка спокою (0, 0)')
plt.plot(N1_eq2, N2_eq2, 'ro', label=f'Точка спокою ({N1_eq2:.1f}, 0)')
plt.plot(N1_eq3, N2_eq3, 'ro', label=f'Точка спокою (0, {N2_eq3:.1f})')

plt.legend()
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Визначаємо диференціальне рівняння
def population_model(N, t, beta, delta, p):
    return beta * N**2 / (1 + N) - delta * N - p * N**2

# Коефіцієнти
beta = 1
delta = 0.1
p = 0.4

# Часові точки
t = np.linspace(0, 10, 200)

# Сценарії початкових умов
initial_conditions = {
    'a': 0.125,  # менше, ніж половина нижньої критичної межі
    'b': 0.185,  # більше, ніж половина нижньої критичної межі
    'c': 0.25,  # дорівнює нижній критичній межі
    'd1': 0.525, # в межах, менше, ніж половина різниці
    'd2': 0.725, # в межах, більше, ніж половина різниці
    'e': 1.0,  # дорівнює верхній критичній межі
    'f': 1.2   # перевищує верхню межу
}

# Розв'язуємо диференціальне рівняння для кожної початкової умови
solution = {}
for key in initial_conditions:
    N0 = initial_conditions[key]
    solution[key] = odeint(population_model, N0, t, args=(beta, delta, p))

# Малюємо результати
plt.figure(figsize=(12, 8))
for key in solution:
    plt.plot(t, solution[key], label=f'Початкова умова {key}')

plt.title('Динаміка популяції з плином часу')
plt.xlabel('Час')
plt.ylabel('Розмір популяції (N)')
plt.legend()
plt.grid(True)
plt.show()
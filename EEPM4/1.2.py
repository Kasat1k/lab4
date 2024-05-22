import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Диференціальне рівняння для зростання популяції 
def population_model(N, t):
    return -0.001 * N**2 + 0.15 * N

# Розрахунок рівноважного розміру популяції (де dN/dt = 0)
def calculate_equilibrium():
    #0, N = 0 або N = 100
    return 100  # Тільки позитивне, ненульове рівноважне значення

initial_conditions = {
    '20_p': 20,
    '180_p': 180
}

# Точки часу для симуляції до 60 місяців
t_long_term = np.linspace(0, 60, 300)

# Розв'язуємо диференціальне рівняння для кожної початкової умови на довгий термін
long_term_solution = {}
for key in initial_conditions:
    N0 = initial_conditions[key]
    long_term_solution[key] = odeint(population_model, N0, t_long_term)

# Знаходимо популяцію на т = 30 місяців для обох початкових умов
t_specific = 30
population_at_30_months = {}
for key in initial_conditions:
    N0 = initial_conditions[key]
    population_at_30_months[key] = odeint(population_model, N0, [0, t_specific])[-1][0]

# Вивід популяції за 6 місяців до консолі
print(f"Популяція на т = 30 місяців для 20 осіб: {population_at_30_months['20_p']}")
print(f"Популяція на т = 180 місяців для 180 осіб: {population_at_30_months['180_p']}")

# Визначення рівноважного розміру популяції
equilibrium = calculate_equilibrium()

# Додатковий аналіз на кінець періоду симуляції
for key, solution in long_term_solution.items():
    final_population = solution[-1][0]
    if final_population > equilibrium:
        status = 'перевищує межу ємності.'
    elif final_population < equilibrium:
        status = 'нижче межі ємності.'
    else:
        status = 'стабілізується на межі ємності.'
    print(f"Кінцева популяція для {key} після 12 місяців {status}")

# Малюємо результати для обох сценаріїв
plt.figure(figsize=(12, 8))
for key in long_term_solution:
    plt.plot(t_long_term, long_term_solution[key], label=f'Початкова умова: {key}')
    plt.axhline(y=equilibrium, color='red', linestyle='--', label='Рівноважна популяція' if key == '20' else None)
plt.title('Динаміка популяції з плином часу')
plt.xlabel('Час (місяці)')
plt.ylabel('Розмір популяції (N)')
plt.legend()
plt.grid(True)
plt.show()
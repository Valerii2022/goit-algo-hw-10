from pulp import LpMaximize, LpProblem, LpVariable, LpStatus

model = LpProblem(name="production-optimization", sense=LpMaximize)

lemonade = LpVariable(name="lemonade", lowBound=0, cat='Continuous')
juice = LpVariable(name="juice", lowBound=0, cat='Continuous')

model += (2 * lemonade + juice <= 100, "Water")
model += (lemonade <= 50, "Sugar")
model += (lemonade <= 30, "Lemon_juice")
model += (2 * juice <= 40, "Fruit_puree")

model += lemonade + juice

model.solve()

print(f"Статус: {model.status}, {LpStatus[model.status]}")
print(f"Кількість Лимонаду: {lemonade.varValue}")
print(f"Кількість Фруктового соку: {juice.varValue}")
print(f"Максимальна кількість продуктів: {model.objective.value()}")

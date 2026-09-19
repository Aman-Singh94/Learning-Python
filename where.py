#np.where(condition, value_if_true, value_if_false)
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])

result = np.where(a % 2 == 0, "Even", "Odd")

print(result)

#salary
salary = np.array([25000, 45000, 30000, 70000, 20000])

bonus = np.where(salary >= 40000, 5000, 2000)

print(bonus)
double=lambda x: x * 2
add=lambda x, y: x + y
subtract=lambda x, y: x - y
multiply=lambda x, y: x * y
divide=lambda x, y: x / y if y != 0 else "Cannot divide by zero"
greater=lambda x, y: x if x > y else y
power=lambda x, y: x ** y
print(double(5))
print(add(3, 4))
print(subtract(10, 5))
print(multiply(3, 4))
print(divide(10, 2))
print(greater(5, 10))
print(power(2, 3))

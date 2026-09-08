print("===== CALCULATOR =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result:", result)


# Save history
file = open("Calculator.txt", "a")

file.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")

file.close()


# Read history
print("\n===== CALCULATION HISTORY =====")

file = open("Calculator.txt", "r")

history = file.read()

print(history)

file.close()
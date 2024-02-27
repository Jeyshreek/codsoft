def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

print("Select your operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("the add is:",num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print("the subtract is:",num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print("the multiply is:",num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print("the divide is:",num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")

num1 = (float(input("Enter num1: ")))
num2 = (float(input("Enter num2: ")))
op = input("Enter operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("not valid number")    
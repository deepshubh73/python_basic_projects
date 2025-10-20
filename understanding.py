# Single input with operator
data = input("Enter expression (like 10+20): ")

# Remove spaces
data = data.replace(" ", "")

# Find operator and split
for op in '+-*/':
    if op in data:
        value1, value2 = data.split(op)
        value1 = int(value1)
        value2 = int(value2)

        # Calculate
        if op == '+':
            result = value1 + value2
        elif op == '-':
            result = value1 - value2
        elif op == '*':
            result = value1 * value2
        elif op == '/':
            result = value1 // value2   # integer division

        print(value1, op, value2, "=", result)
        break

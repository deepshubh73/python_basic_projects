

data = input("Enter expression (e.g., 10 + 20): ")

# Split by space
parts = data.split()  # ['10', '+', '20']
data = data.replace(' ', '')

if len(parts) != 3:
    print("Error: please enter in format: value1 operator value2")
else:
    value1, operator, value2 = parts

for op in '+-*/':
    if op in data:
        value1_str, value2_str = data.split(op)

if op == "+":
    result = value1 + value2
    print(f"{value1} {operator} {value2} = {result}")

elif op =="-":
    result1 = value1 - value2
    print(f"{value1} {operator} {value2} = {result1}")
    
elif op == "*":
    result3 = value1 * value2
    print(f"{value1} {operator} {value2} = {result3}")
   
# elif op == "/":
#     result4 = value1 / value2
    #   print(f"{value1} {operator} {value2} = {result4}")
    

else:
    print("invalid operator")

# print(f"{value1} {operator} {value2} = {result}")

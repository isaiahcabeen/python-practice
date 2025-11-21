x = int(input("Whats x: "))
y = int(input("Whats y: "))
op = input("Whats the operator (*, /, +, -): ")

if op == "*":
	print(x * y)
elif op == "/":
	print(x / y)

elif op == "+":
	print(x + y)
else:
	print(x - y)

expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

if y == "+":
    t = float(x) + float(z)
elif y == "-":
    t = float(x) - float(z)
elif y == "*":
    t = float(x) * float(z)
elif y == "/":
    t = float(x) / float(z)
else:
    t = 0.0

x = float(input("What's x?"))
y = float(input("What's y?"))

z = x + y
print(z)

# Create a rounded result
z = round(x + y)
print(z)

# Print the formatted result
print(f"{z:,}")

# Division
z = x/y
print(z)

# Division with round
z = round(x/y,2)
print(z)

# Print the formatted result `fstring`
print(f"{z:.2f}")
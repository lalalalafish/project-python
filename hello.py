# Ask the user for their name
name = input("What's your name?").strip().title()

# Print hello and the inputted name
print("Hello,", name)

# Test end argument
print("Hello,",end="")
print(name)

# Formatting strings
print(f"Hello,{name}")


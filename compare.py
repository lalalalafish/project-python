x = int(input("What's x?"))
y = int(input("What's y?"))

# equal
if x == y:
    print("x is equal to y")
else:
    print("Sorry x is not equal to y")

# not
if x != y:
    print("Sorry x and y are not equal")
else:
    print("x and y are equal")

# or
if x < y or x > y:
    print("Sorry x and y are not equal")
else:
    print("x is equal to y")

# if control flow
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# elif control flow
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

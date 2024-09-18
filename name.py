name = input("What's your name?")

# match
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Who?")

if name == "Harry":
    print("Gryffindor!")
elif name == "Hermione":
    print("Gryffindor!")
elif name == "Ron":
    print("Gryffindor!")
elif name == "Slytherin":
    print("Slytherin!")
else:
    print("Who?")


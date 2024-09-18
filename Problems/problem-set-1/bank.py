greeting = input("Greeting: ").strip().lower()
inital = greeting[0:5]
if greeting[0:4] == "hello":
    print("$0")
elif greeting[0] == 'h':
    print("$20")
else:
    print("$100")

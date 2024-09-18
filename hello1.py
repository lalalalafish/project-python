# We don't have to have our function at the start of our program
# Use run to restore the order
def main():
    # Ask the user for their name
    name = input("What's your name?").strip().title()
    hello(name)
    hello()


def hello(to="world"):
    print("hello,", to)

# Need to call main() otherwise nothing will happen
main()
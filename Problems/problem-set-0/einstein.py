def main():
    mass = int(input("Please input the mass in kilograms: "))

    energy = mass * square(300000000)
    print(energy)

def square(x):
    return x * x


main()
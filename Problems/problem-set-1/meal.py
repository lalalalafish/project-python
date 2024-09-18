def main():
    time = input("What time is it?").strip()
    time = convert(time)
    if 7 <= time < 8:
        print("breakfast time")
    elif 12 <= time < 13:
        print("lunch time")
    elif 18 <= time < 19:
        print("dinner time")


def convert(time):
    x = float(time.split(':')[0])
    y = float(time.split(':')[1])
    return x + y / 60


if __name__ == "__main__":
    main()

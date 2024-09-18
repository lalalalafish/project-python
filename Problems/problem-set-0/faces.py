def main():
    sentence = input("Please enter a sentence: ")
    sentence = convert(sentence)
    print(sentence)


# The definition of convert function
def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence


main()

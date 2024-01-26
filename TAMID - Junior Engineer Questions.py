
def isPalindrome(string):
    # one liner to check if string is a palindrome
    print(f"{string} is a pal") if string == string[::-1] else print(f"{string} is not a pal")


def boxedStrings(list):
    # gets width of box
    width = len(max(list, key=len)) + 4

    # prints top border
    print("*" * width)
    for word in list:
        wordToPrint = f"* {word}"
        # Determines how much whitespace needed within each line of the box
        extraWhiteSpace = width - len(wordToPrint) - 1

        # prints all content within the box
        print(f"* {word}", end="")
        print(" " * extraWhiteSpace, end="")
        print("*")

    # prints bottom border
    print("*" * width)
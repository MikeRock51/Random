#!/usr/bin/python3


def truncate(s, k):
    # Split the string
    splitStr = s.split()

    # Extract the first k words
    splitStr = splitStr[:k]

    # Combine all words into a sentence
    splitStr = " ".join(splitStr)

    # Returning our sentence
    return(splitStr)

print(truncate("What is the solution to the problem", 5))

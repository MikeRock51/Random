def lengthLastWord(s):
    if len(s) == 0:
        return (0)
    if len(s) == 1:
        return(1)
    words = s.split()

    return len(words[-1])

print(lengthLastWord("Hello World"))

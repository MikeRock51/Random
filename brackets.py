def brackets(str):
    if not str:
        return (1)

    openBrackets = ['[', '{', '(']
    closeBrackets = [']', '}', ')']
    closed = True
    open = 0
    openType = ""
    closeType = ""

    for c in str:
        if c in openBrackets:
            closed = False
            open += 1
            if str.index(c) == 0:
                openType = c
        if c in closeBrackets:
            closed = True
            open -= 1
            closeType = c

    if closed == True and open == 0 and closeBrackets.index(closeType) == openBrackets.index(openType):
        return (1)

    return (0)


print(brackets("(johndoe)"))
print(brackets("([)]"))
print(brackets("{[(0 + 0)(1 + 1)](3*(-1)){()}}"))
print(brackets(""))

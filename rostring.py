def rostring(str):
    if str == "":
        return ""

    stripped = str.strip()
    words = stripped.split(' ')

    print(words)

    first_word = words[0]
    del(words[0])
    words.append(first_word)
    word_str = ""
    separator = ' '

    word_str = separator.join(wrd for wrd in words)
    return (word_str)

print(rostring("Que la      lumiere soit et la lumiere fut"))
print(rostring("     AkjhZ zLKIJz , 23y"))
# print(rostring("abc "))

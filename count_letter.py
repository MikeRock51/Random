def count_letter(str):

    uniqs = ''
    letter_counts = []
    separator = ', '

    for c in str:
        if c not in uniqs and c.isalpha():
            uniqs += c
    print (uniqs)
    for c in uniqs:
        count = 0
        i = 0
        while (i < len(str)):
            if str[i] == c:
                count += 1
            i += 1
        letter_counts.append(f"{count}{c.lower()}")
    
    return (separator.join(s for s in letter_counts))

print (count_letter("abbcc"))
print (count_letter("My Hyze 47y 7."))

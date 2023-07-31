def hidenp(needle, haystack):
    if not needle:
        return (1)
    elif not haystack:
        return (0)
    
    found = ""
    haystackIdx = 0

    for c in needle:
        for ch in haystack[haystackIdx:]:
            if c == ch:
                found += c
                break
            haystackIdx += 1
    
    # print(found)
    if needle == found:
        return (1)

    return (0)

# print(hidenp("fgex.;","tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"))
# print(hidenp("abc", "btarc"))
# print(hidenp("", "long string ?ddl"))

def capitalize(str):
    if not str:
        return ("")

    if str[0].isalpha() or str[0] == " ":
        return (str.title())
    else:
        cap = str.split()[0]
        i = 0
        while str[i] != " ":
            i += 1
    cap += str[i:]
    return (cap)
    

print(capitalize("__second Test A Little Bit   Moar Complex"))
print(capitalize("   But... This iS not THAT COMPLEX"))

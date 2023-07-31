def str_maxlenoc(arr, len):
    if not arr:
        return ("")

    pat = ""
    in_it = True
    t = ""
    for str in arr:
        t = ""
        for c in str:
            t += c
            for s in arr:
                # print(f"c {t} {t in s} {s}")
                if not t in s:
                    in_it = False
                    t = ""
                    break
                else:
                    in_it = True
                # print(f"t {t}")
            if t.__len__() > pat.__len__():
                pat = t
            # print(f"pat: {pat}")

    return (pat)
                    

    

print(str_maxlenoc(["ab", "bac", "abacabccabcb"], 3))
print(str_maxlenoc(["bonjour", "salut", "bonjour", "bonjour"], 4))
print(str_maxlenoc(["xoxAoxo", "xoxAox", "oxAox"], 3))

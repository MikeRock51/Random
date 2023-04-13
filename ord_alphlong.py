def ord_alphlong(str):
	if not str:
		return ""
          
	wordSplit = str.split()
	lenSort = sorted(wordSplit, key=lambda x: (len(x), x[0].lower(), x[1:]))

	jointStr = ""

	s = 0
	while s < len(lenSort):
		jointStr += lenSort[s]
		if s < len(lenSort) - 1:
			if len(lenSort[s]) == len(lenSort[s + 1]):
				jointStr += " "
			else:
				jointStr += "^"
		s += 1

	return (jointStr)

print(ord_alphlong( "After all this time Always said Snape"))
print(ord_alphlong("A a b B cc ca cd"))

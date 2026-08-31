def mw(w):
    ctr = 0
    lst = []
    for word in w:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of words with first and last character same\n", lst)
    return ctr

c = mw(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and last character same: ", c)    
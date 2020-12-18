def palindromicPermutation(word: str) -> bool:
    x = form_dict(word)
    oddFound = False
    for i in x.values():
        if i % 2 is 1:
            if oddFound:
                return False
            else:
                oddFound = True
    return True


def form_dict(word: str) -> dict:
    x = {}
    for i in word:
        if i in x.keys():
            x[i] += 1
        else:
            x[i] = 1
    return x


print(palindromicPermutation("vikattkavi"))

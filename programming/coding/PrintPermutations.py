def toStr(list):
    return ''.join(list)

def permute(s, l, r):
    """
    Function to find permutations of a given sting
    :arg s : string,
    :arg l : left element of the string,
    :arg r : right element of the string.
    """
    if l==r:
        print(toStr(s))
    for i in range(l, r):
        s[i], s[l] = s[l], s[i]
        permute(s, l + 1, r)
        s[i], s[l] = s[l], s[i] # backtrack

s = input('Enter a string:')
n = len(s)
a = list(s)
permute(a, 0, n)

    
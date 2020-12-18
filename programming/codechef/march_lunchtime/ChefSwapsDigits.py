def swap(y, x, a, b):
    temp = a[y]
    a[y] = b[x]
    b[x] = temp


def printWithAdd(a, b):
    p =combineListToInt(a)
    q = combineListToInt(b)
    print(p+q)

def combineListToInt(lst):
    return int(''.join(map(str, lst)))

for _ in range(int(input())):
    x = [int(i) for i in input().split()]
    p = min(x)
    q = max(x)

    a = list(map(int, str(p)))
    b = list(map(int, str(q)))

    if len(a)>1 and len(b) > 1:
        if a[1] > b[0]:
            swap(1,0, a,b)
        elif a[1] > a[0]:
            swap(0,1,a,b)
    elif len(b) > 1:
        if a[0] > b[0]:
            swap(0, 0, a, b)
    printWithAdd(a, b)


#Pintu and Fruits
from array import array

for x in range(int(input())):
    arr = [int(j) for j in input().split()]
    n = arr[0]
    m = arr[1]
    f = [int(y) for y in input().split()]
    p = [int(z) for z in input().split()]

    fruit_arr = array('I', (0 for c in range(m)))

    for j in range(n):
        fruit_arr[f[j] -1] += p[j]

    print(min(filter(lambda x: x>0, fruit_arr)))


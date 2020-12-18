for x in range(int(input())):
    size = int(input())
    p = [int(k) for k in input().split()]
    q = [int(k) for k in input().split()]
    p.sort()
    q.sort()
    s=0
    for i in range(size):
        s+=min(p[i],q[i])
    print(s)



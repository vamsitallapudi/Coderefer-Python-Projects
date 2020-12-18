# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if(a//10==0 and b//10==0):
        print(a+b)
    elif(a//10==0):
        p1=a+b
        p2=a*10+b%10+b//10
        print(max(p1,p2))
    elif(b//10==0):
        q1=a+b
        q2=b*10+a%10+a//10
        print(max(q1,q2))
    else:
        t1=a+b
        t2=a%10+a//10+(b%10)*10+(b//10)*10
        t3=b%10+b//10+(a%10)*10+(a//10)*10
        print(max(t1,t2,t3))
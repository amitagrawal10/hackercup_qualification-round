t=int(input())
for j in range(1,t+1):
    n,k=[int(x) for x in input().split()]
    a,b,c,r=[int(x) for x in input().split()]
    print(n,k,a,b,c,r)
    m=[]
    m.append(a)
    print(m)
    for i in range(1,n+1):
        m.append(((b * m[i - 1] + c) % r))
        print(m)
    print("case #{}: {}".format(j,m[n]))
    
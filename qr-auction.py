t= int(input())
for k in range(1,t+1):
    n,p1,w1,m,k,a,b,c,d=[int(x) for x in input().split()]
    price=[]
    weight=[]
    price.append(p1)
    weight.append(w1)
    bar_cnt=0
    ter_cnt=0
    for i in range(n):
        p = ((((a* price[i])  -1) + b) % m) + 1 
        w = ((((c* weight[i]) -1) + d) % k) + 1
        price.append(p)
        weight.append(w) 
    
    for j in range(len(price)):
        for l in range(len(price)):
            if(j!=l):  
                if(((price[j]<=price[l])&(weight[j]<weight[l])) |((price[j]<price[l])&(weight[j]<=weight[l]))):
                    bar_cnt+=1
    print(bar_cnt)

                    
    
        
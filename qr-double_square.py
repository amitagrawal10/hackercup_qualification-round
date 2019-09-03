t = int(input())
import math
def issquare(n):
    sqrt=math.sqrt(n)
    is_perfect=sqrt-math.floor(sqrt)
    if(is_perfect==0):
        return True
    else:
        return False
for i in range(1,t+1):
    num=int(input())
    flag=0
    j=0
    list1=[]
    while(flag==0):
        n=num-(j*j)
        if(n<=0):
            flag=1
        elif(issquare(n)):
            list1.append(j)
        j+=1
    set1=set(list1)
    print("case #{}: {}".format(i,len(set1)-1))
    
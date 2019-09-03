t=int(input())
import math 
def isPerfectSquare(x): 
	sr = math.sqrt(x)  
	return ((sr - math.floor(sr)) == 0)
for i in range(1,t+1):
    list1=[str(x) for x in input().split()]
    print(list1)
    w=int(list1.pop(0))
    h=int(list1.pop(0))#list is updated after first pop,hence index 0 again
    print(w,h)
    s=" "
    text =s.join(list1)
    print(text)
    len1=len(text)
    print(len1)
    words=text.split()
    max_size=max([len(x) for x in words])
    max_hight=len(words)
    print(words)
    print(max_size)
    area=w*h
    flag=0
    farea=area//len1
    print(farea)
    while(flag==0):
        if(isPerfectSquare(farea)):
            size=math.sqrt(farea)
            print(size)
            if(((size*max_size)<=w)&((size*max_hight)<=h)):
                flag=1
        farea-=1
    print("case #{}: {}".format(i,size))



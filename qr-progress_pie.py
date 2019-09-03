t=int(input())
import math
for i in range(1,t+1):
    p,x,y=[int(x) for x in input().split()]
    if(p==0):
        print("case #{}: {}".format(i,"white"))
        print("0")
    else:
        if(math.sqrt(((x-50)**2)+((y-50)**2)) >50):
            print("case #{}: {}".format(i,"white"))
            print("1")
        elif(((p/100)*2*math.pi)>(math.atan2(y,x))):
            print("case #{}: {}".format(i,"black"))
            print("3")
        else:
            print("case #{}: {}".format(i,"white"))
            print("4")
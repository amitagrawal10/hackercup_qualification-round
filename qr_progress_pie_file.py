file1=open("progress_pie.txt","r+")
file2=open("result.txt","w")
t=int(file1.readline())

import math
for i in range(1,t+1):
    p,x,y=file1.readline().split()
    p=int(p)
    x=int(x)
    y=int(y)
    if(p==0):
        file2.write("case #{}: {}".format(i,"white\n"))
    else:
        if(math.sqrt(((x-50)**2)+((y-50)**2)) >50):
            file2.write("case #{}: {}".format(i,"white\n"))
        elif(((p/100)*2*math.pi)>(math.atan2(y,x))):
            file2.write("case #{}: {}".format(i,"black\n"))
        else:
            file2.write("case #{}: {}".format(i,"white\n"))
file1.close()
file2.close
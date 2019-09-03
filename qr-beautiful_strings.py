t=int(input())
from collections import defaultdict
for i in range(1,t+1):
    text=str(input())
    text=text.upper()
    letters=defaultdict(int)
    for letter in text:
        letters[letter]+=1
   # print(letters)

    items=list(letters.items())
    #print(items)
    #print(len(items))
    values=list(letters.values())
    #print(values)
    z=26
    dict1={}
    for k in range(len(items)):
        flag=0
        if(len(values)!=0):
            maximum=max(values)
            #print(maximum)
            for l in items:
                if(l[1]==maximum):
                    values.remove(maximum)
                    #print(values)
                    items.remove(l)
                    if((l[0]>='A')& (l[0]<='Z')):
                        dict1[l[0]]=z
                        z-=1   
    print(dict1)
    beauty_value=0
    text1=[]
    for d in text:
        if((d>='A') & (d<='Z')):
            text1.append(d)
    for c in text1:
        print(c)
        beauty_value+=dict1.get(c)
    print("case #{}: {}".format(i,beauty_value))


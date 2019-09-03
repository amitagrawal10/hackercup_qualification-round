t=int(input())
for i in range(1,t+1):
    n=int(input())
    num=str(n)
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    for x in num:
        list1.append(x)
    while(len(list1)!=0):
        j=max(list1)
        list2.append(j)
        list1.remove(j)
    maxi=int(''.join(list2))
    while(len(list1)!=0):
        mini_first=min(list1)
        if(mini_first==0):
            list1.remove(mini_first)
            list4.append(mini_first)
        else:
            list3.append(mini_first)
            list1.remove(mini_first)
    list5.append(list3[0])
    list3.remove(list3[0])
    while(len(list4)!=0):
        list5.append(list4[0])
        list4.remove(list4[0])
    while(len(list3)!=0):
        list5.append(list3[0])
        list3.remove(list3[0])
    mini=int(''.join(list5))
    print("case #{}: {} {}".format(i,maxi,mini))
        
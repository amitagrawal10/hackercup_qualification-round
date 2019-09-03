t=int(input())
for i in range(1,t+1):
    text=str(input())
    print(text)
    list1=[x for x in text]
    list2=[]
    for j in range(len(list1)):
        if(j<(len(list1)-1)):
            k=list1[j]
            l=list1[j+1]
            if((k==':') & (l in '()')):
                list2.append(k)
            if(k=='(')|(k==')'):
                list2.append(k)
    if((list1[-1]) in '()'):
        list2.append(list1[-1])
    print(list2)
    flag=0#n0
    col=list2.count(':')
    left=list2.count('(')
    right=list2.count(')')
    if(len(list2)!=0):
        if(list2[0]==')'):
            flag=0
        if(right>left | left>right):
            for l1 in range(len(list2)):
                first=list2[l1]
                second=list2[l1+1]
                if(first==':' & second =='('):
                    left-=1
                if(first==':' & second ==')'):
                    right-=1
    if(left==right):
        flag=1
    if(flag==1):
        print("case #{}: {}".format(i,"YES"))
    if(flag==0):
        print("case #{}: {}".format(i,"NO"))
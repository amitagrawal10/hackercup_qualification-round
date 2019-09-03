t=int(input())
for i in range(1,t+1):
    text=str(input())
    list1=text.split()
    list2=[]
    while(len(list1)!=0):
        list2.append(min(list1))
        list1.remove(min(list1))
    lex_string=''.join(list2)
    print("case #{}: {}".format(i,lex_string))

    
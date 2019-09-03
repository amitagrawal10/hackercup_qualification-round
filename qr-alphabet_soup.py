t =int(input())
for k in range(1,t+1):
    string = str(input())
    #print(string)
    list1=[x for x in string]
    #print("list1:",list1)
    list2=['H','A','C','K','E','R','C','U','P']
    print("list2",list2)
    count=0
    for i in list1:
        for j in list2:
            if(i==j):
                list2.remove(j)
               # print("list2",list2)
                if(len(list2)==0):
                    count+=1  
                    list2=['H','A','C','K','E','R','C','U','P']   
    print("case #{}: {}".format(k,count))
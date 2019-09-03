file1=open("test.txt","r+")
file2=open("result.txt","w")
t=int(file1.readline())

for k in range(1,t+1):
    string =file1.readline() 
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
    file2.write("case #{}: {}".format(k,count))
file1.close()
file2.close()

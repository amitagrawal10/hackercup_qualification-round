t= int(input())
list1= [int(x) for x in input().split()] 
print(list1)
flag=0
for i in list1:
    key=i
    while(flag==0):
        for j in list1:
            if(key==j):
                print(key)
                flag=1
                break
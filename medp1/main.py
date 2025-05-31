n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j-1==0):
            print(0,end=" ")
        print(pow(i,j),end=" ")
    print()
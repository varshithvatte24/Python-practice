n = int(input())
print(str(" ")*(n-1)+"*")
for i in range(1,n):
        print(str(" ")*(n-i-1)+"*"+str(" ")*((i*2)-1)+"*")
for j in range(n-1,1,-1):
    print(str(" "*(n-j))+"*"+(str(" ")*((j*2)-3))+"*")
print(str(" ")*(n-1)+"*")
        
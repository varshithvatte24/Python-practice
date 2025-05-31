def pt(n):
    for i in range(n):
        num=1
        for j in range(i+1):
            print(num,end=" ")
            num = num*(i-j)//(j+1)
        print("0 "*(n-i-1))
n=6
pt(n)
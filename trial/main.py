n = int(input())
for i in range(n+1):
    p1 = pow(11,i)
    size =len(str(p1))
    if size < 5:
        rem = n-size
        
    print(str(p1)+("0"*rem));
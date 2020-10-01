def fibnonaci(n):
    a=0
    b=1
    sum=0
    while(sum<n):
        print(sum)
        a=b
        b=sum
        sum=a+b
n=int(input())
fibnonaci(n)
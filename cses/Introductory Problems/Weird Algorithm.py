def Solution():
    n=int(input())
    temp=n
    temp1=0
    temp2=0
    print(n, end=" ")
    while temp>1:
        if temp%2==0:
            temp/=2
            print(int(temp), end =" ")
        else:
            temp=temp*3+1
            print(int(temp), end=" ")

Solution()
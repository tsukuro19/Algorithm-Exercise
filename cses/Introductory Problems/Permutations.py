def Solution(n):
    a=[]
    b=[]
    if n==1:
        print(1)
    elif n<=3:
        print('NO SOLUTION')
    elif n==4:
        print(2,4,1,3)
    else:
        for i in range(n,0,-1):
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        # * used to delete []
        print(*(a+b))

n=int(input())
Solution(n)
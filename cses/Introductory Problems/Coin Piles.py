def Coin_Piles(a,b):
    i=1
    a_swap=0
    b_swap=0
    if a>b:
        a_swap,b_swap=a,b
    else:
        a_swap,b_swap=b,a
    while a_swap>0 and b_swap>0:
        if i%2!=0:
            a_swap-=2
            b_swap-=1
        else:
            a_swap-=1
            b_swap-=2
        i+=1
    if a_swap==0 and b_swap==0:
        print('YES')
    else:
        print('NO')
t=int(input())
while t>0:
    a,b=map(int,input().split(' '))
    Coin_Piles(a,b)
    t-=1
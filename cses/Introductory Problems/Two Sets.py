def Two_Sets(n):
    s=(n*(n+1))//2
    sub_s=s//2
    a=set()
    b=set()
    if s%2!=0:
        print('NO')
    else:
        for i in range(n,0,-1):
            if i<=sub_s:
                sub_s-=i
                a.add(i)
            else:
                b.add(i)
        print('YES')
        print(len(a))
        print(*a)
        print(len(b))
        print(*b)

n=int(input())
Two_Sets(n)
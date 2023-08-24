def utopian(n):
    result=0
    for i in range(n+1):
        if i%2==0:
            result+=1
        else:
            result*=2
    return result

t=int(input())
for i in range(t):
    n=int(input())
    print(utopian(n))
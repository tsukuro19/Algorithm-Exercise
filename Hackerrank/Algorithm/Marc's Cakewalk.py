def Solution(n,a):
    sum=0
    for i in range(0,n):
        sum=sum+max(a)*pow(2,i)
        a.remove(max(a))
    return sum

n=int(input())
a = list(map(int,input().strip().split()))[:n]
print(Solution(n,a))
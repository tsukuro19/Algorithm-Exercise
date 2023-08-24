def Solution(a,n):
    count=0
    for i in range(n-1):
        if a[i+1]<=a[i]:
            diff=a[i]-a[i+1]
            count+=a[i]-a[i+1]
            a[i+1]+=diff
    return count

n=int(input())
a=list(map(int,input().strip().split()))[:n]
print(Solution(a,n))
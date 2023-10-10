n=int(input())
a=list(map(int,input().split()))
a.sort()
diff=[]
for i in range(n-1):
    diff.append(abs(a[i]-a[i+1]))
print(min(diff))
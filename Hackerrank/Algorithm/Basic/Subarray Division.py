def SubArray_Division(s,d,m):
    count=0
    for i in range(0,len(s)-m+1):
        if sum(s[i:i+m])==d:
            count+=1
    return count

n=int(input())
s=list(map(int,input().split()))
d,m=map(int,input().split())
print(SubArray_Division(s,d,m))
def Count_time(n,k,times):
    count=0
    for i in range(n):
        if times[i]<=0:
            count+=1
    return "NO" if count>=k else "YES"

if __name__=="__main__":
    test=int(input())
    for _ in range(test):
        n,k=map(int,input().split())
        times=list(map(int,input().split()))
        print(Count_time(n,k,times))
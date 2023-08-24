import math
def Sale_By_Match(a):
    list_count=[]
    count=1
    for i in range(1,len(a)):
        if a[i-1]==a[i]:
            count+=1
        else:
            if count==1:
                continue
            else:
                list_count.append(math.floor(count/2))
                count=1
    return sum(list_count)


n=int(input())
arr=list(map(int,input().split()))
print(Sale_By_Match(sorted(arr)))
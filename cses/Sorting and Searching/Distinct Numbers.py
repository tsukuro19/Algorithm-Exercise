def Distinct_Numbers(n,list_n):
    set_list=set(list_n)
    return len(set_list)


n=int(input())
list_n=list(map(int,input().split()))
print(Distinct_Numbers(n,list_n))
def Luck_Balance(luck,rate,dict_contest,k):
    sum_luck=0
    min_dict=0
    min_key=0
    i=1
    if rate.count(1)==k:
        sum_luck+=sum(luck)
    else:
        while i:
            if dict_contest[min(dict_contest.keys())]!=1:
                dict_contest.pop(dict_contest[min(dict_contest.keys())])
            else:
                min_dict+=min(dict_contest.keys())
                break
        luck.remove(min_dict)
        sum_luck=sum_luck+sum(luck)-min_dict
    return sum_luck


n,k=map(int,input().split(' '))
dict_contest={}
luck=[]
rate=[]
for i in range(n):
    x=list(map(int,input().strip().split()))
    dict_contest[x[0]]=x[1]
    luck.append(x[0])
    rate.append(x[1])
print(Luck_Balance(luck,rate,dict_contest,k))
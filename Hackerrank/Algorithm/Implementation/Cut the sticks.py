def return_all(list,target):
    return [i for i in list if i!=target]

def Cut_stick(sticks):
    result=[]
    while sticks!=[]:
        min_stick=min(sticks)
        result.append(len(sticks))
        for i in range(len(sticks)):
            sticks[i]-=min_stick
        sticks=return_all(sticks,0)
    return result


if __name__=="__main__":
    n=int(input())
    sticks=list(map(int,input().split()))[:n]
    for i in Cut_stick(sticks):
        print(i)
    
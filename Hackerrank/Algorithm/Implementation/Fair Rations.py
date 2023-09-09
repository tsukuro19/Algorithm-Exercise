def Fair_rations(loaf):
    result=0
    for i in range(len(loaf)-1):
        if loaf[i]%2!=0:
            loaf[i]+=1
            loaf[i+1]+=1
            result+=2
    if loaf[-1]%2!=0:
        return "NO"
    else:
        return result


if __name__=="__main__":
    number=int(input())
    loaf=list(map(int,input().split()))
    print(Fair_rations(loaf))
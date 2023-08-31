def Jumping_cloud(n,clouds):
    index,count=0,0
    while index!=n-1:
        if index+2>n-1:
            count+=1
            index+=1
        else:
            if clouds[index+2]==0:
                count+=1
                index+=2
            else:
                count+=1
                index+=1
    return count


if __name__=="__main__":
    n=int(input())
    clouds=list(map(int,input().split()))
    print(Jumping_cloud(n,clouds))
if __name__=="__main__":
    number,test=map(int,input().split())
    lanes=list(map(int,input().split()))
    while test!=0:
        start,end=map(int,input().split())
        print(min(lanes[start:end+1]))
        test-=1
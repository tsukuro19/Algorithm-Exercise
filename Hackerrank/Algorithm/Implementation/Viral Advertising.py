def Viral(n,count,recipient):
    if n==1:
        return count
    return count+Viral(n-1,((recipient//2)*3)//2,(recipient//2)*3)


if __name__=="__main__":
    n=int(input())
    count,recipient=2,5
    print(Viral(n,count,recipient))
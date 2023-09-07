def Chocolate_Feast(cost,price,m):
    total_chocolate=cost//price
    wraps=total_chocolate
    if total_chocolate<m:
        return total_chocolate
    else:
        while wraps>=m:
            total_chocolate+=wraps//m
            wraps=wraps//m+wraps%m
        return total_chocolate


if __name__=="__main__":
    test=int(input())
    while test!=0:
        cost,price,m=map(int,input().split())
        print(Chocolate_Feast(cost,price,m))
        test-=1